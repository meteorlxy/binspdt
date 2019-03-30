import os
import shutil
import time
import tempfile
import traceback

import random
import string

from django.core.paginator import Paginator
from django.db.models import Q

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from binary.models import Module, ModuleObject, ModuleAnalysis
from binary.serializers import ModuleSerializer
from binary.utils import db
from binary.core.asm import Module as AsmModule, Instruction as AsmInstruction

class Modules(ViewSet):
  """
  Handle modules request
  """
  def index(self, request, format='json'):
    """
    Get modules list
    """
    # get fields of modules
    module_fields = tuple(field.name for field in Module._meta.get_fields())
    queryset = Module.objects.all()

    # get pagination params from query
    params = {
      'paginate': request.GET.get('_paginate', 'true').lower(),
      'page': request.GET.get('_page', 1),
      'per_page': request.GET.get('_per_page', 25),
      'order_by': request.GET.get('_order_by', '-id'),
      'search': request.GET.get('_search', ''),
    }

    if params['search'] != '':
      queryset = queryset.filter(
        Q(name__contains = params['search'])
        | Q(architecture__contains = params['search'])
        | Q(md5__contains = params['search'])
        | Q(import_time__contains = params['search'])
      )

    if params['order_by'] not in module_fields:
      params['order_by'] = '-id'

    queryset = queryset.order_by(params['order_by'])

    if params['paginate'] != 'false':
      paginator = Paginator(queryset, params['per_page'])
      page = paginator.get_page(params['page'])
      data = ModuleSerializer(page.object_list, many=True).data

      return Response({
        'page': page.number,
        'page_count': paginator.num_pages,
        'data': data,
        'count': paginator.count,
      })
    else:
      data = ModuleSerializer(queryset, many=True).data
      return Response({
        'data': data,
      })

  def count(self, request, format='json'):
    """
    Get modules count
    """
    return Response({
      'data': Module.objects.count(),
    })

  def details(self, request, module_id, format='json'):
    """
    Get module details
    """
    queryset = Module.objects.get(id=module_id)
    data = ModuleSerializer(queryset).data
    data['details'] = db.get_module_details(module_id)
  
    return Response({
      'data': data,
    })
  
  def _delete_one_module(self, module_id):
    # Delete all analyses related to this module
    ModuleAnalysis.objects.filter(Q(module_1_id=module_id) | Q(module_2_id=module_id)).delete()
    # Delete the module itself
    db.delete_module(module_id)

  def delete(self, request, module_id, format='json'):
    """
    Delete one module
    """
    try:
      self._delete_one_module(module_id=module_id)
      return Response({
        'msg': 'deleted module successfully',
        'data': {
          'module_id': module_id
        }
      }, status=status.HTTP_200_OK)
    except Exception:
      return Response({
        'msg': 'failed to delete module #' + module_id,
      }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def delete_many(self, request, format='json'):
    """
    Delete many modules according to id
    """
    modules = request.data['modules']
    try:
      for module_id in modules:
        self._delete_one_module(module_id=module_id)
      return Response({
        'msg': 'deleted modules successfully',
        'data': {
          'modules': modules
        }
      }, status=status.HTTP_200_OK)
    except Exception:
      return Response({
        'msg': 'failed to delete modules',
        'data': {
          'modules': modules
        }
      }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  
  def create(self, request, file_type, ida_version, format='json'):
    """
    Create a module from uploaded idb file
    """
    try:
      # Get the upload files list
      upload_files = request.FILES.getlist('file')

      for upload_file in upload_files:
        # Save the uploaded file to temp dir
        tmp_dir = os.path.join(tempfile.gettempdir(), 'binspdt.%s.%s' % (
          time.strftime('%Y%m%d%H%M%S', time.localtime()),
          ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        ))
        tmp_filename = os.path.join(tmp_dir, upload_file.name)
        if not os.path.exists(tmp_dir):
          os.makedirs(tmp_dir)
        with open(tmp_filename, 'wb') as f:
          for chunk in upload_file.chunks(): 
            f.write(chunk)

        try:
          if file_type == 'idb':
            # Import the uploaded idb file
            db.import_idb(file=tmp_filename, version=ida_version)
          elif file_type == 'x86_32':
            # Import the uploaded binary file
            db.import_bin(file=tmp_filename, x64=False, version=ida_version)
          elif file_type == 'x86_64':
            # Import the uploaded binary file
            db.import_bin(file=tmp_filename, x64=True, version=ida_version)
          else:
            return Response({
              'msg': 'files type not allowed',
            }, status=status.HTTP_400_BAD_REQUEST)
        finally:
          # Delete the uploaded file from temp dir
          shutil.rmtree(tmp_dir)
      return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
      print(traceback.format_exc())
      return Response({
        'msg': 'failed to create module',
      }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def module_functions(self, request, module_id, format='json'):
    """
    Get module functions
    """
    return Response({
      'data': db.get_module_functions(module_id=module_id),
    })

  def function_basic_blocks(self, request, module_id, function_address, format='json'):
    return Response({
      'data': db.get_function_basic_blocks(module_id=module_id, function_address=function_address),
    })

  def basic_block_instructions(self, request, module_id, function_address, basic_block_id, format='json'):
    inst_list = db.get_basic_block_instructions(module_id=module_id, function_address=function_address, basic_block_id=basic_block_id)
    asm_module = AsmModule(db, module_id)
    data = list()
    for inst in inst_list:
      asm_inst = AsmInstruction(asm_module, inst)
      asm_inst.load_operands()
      data.append({
        'address': asm_inst.address,
        'mnemonic': asm_inst.mnemonic,
        'operands': map(lambda item: item.symbol, asm_inst.operands.values()),
      })
    return Response({
      'data': data,
    })
