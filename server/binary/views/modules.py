import os
import time
import tempfile

from django.core.paginator import Paginator
from django.db.models import Q

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from binary.models import Module, ModuleObject, ModuleResult
from binary.serializers.module import ModuleSerializer
from binary.utils import analysis, db

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
    qeuryset = Module.objects.all()

    # get pagination params from query
    params = {
      'page': request.GET.get('_page', 1),
      'per_page': request.GET.get('_per_page', 25),
      'order_by': request.GET.get('_order_by', 'id'),
      'search': request.GET.get('_search', ''),
    }

    if params['order_by'] not in module_fields:
      params['order_by'] = 'id'

    if params['search'] != '':
      qeuryset = qeuryset.filter(
        Q(name__contains = params['search'])
        | Q(architecture__contains = params['search'])
        | Q(md5__contains = params['search'])
        | Q(import_time__contains = params['search'])
      )

    qeuryset = qeuryset.order_by(params['order_by'])
    paginator = Paginator(qeuryset, params['per_page'])
    page = paginator.get_page(params['page'])
    data = ModuleSerializer(page.object_list, many=True).data

    return Response({
      'page': page.number,
      'page_count': paginator.num_pages,
      'data': data,
      'count': paginator.count,
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
    Get module detail
    """
    return Response({
      'data': db.get_module_details(module_id),
    })

  def delete(self, request, module_id, format='json'):
    """
    Delete one module
    """
    try:
      # Delete all related analysis results
      results = ModuleResult.objects.filter(Q(module_1_id=module_id) | Q(module_2_id=module_id))
      for result in results:
        analysis.delete(result.path)
      # Delete the module itself
      db.delete_module(module_id)
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
        # Delete all related analysis results
        results = ModuleResult.objects.filter(Q(module_1_id=module_id) | Q(module_2_id=module_id))
        for result in results:
          analysis.delete(result.path)
        # Delete the module itself
        db.delete_module(module_id)
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
          'module_id': modules
        }
      }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  
  def create(self, request, ida_version, format='json'):
    """
    Create a module from uploaded idb file
    """
    try:
      # Get the upload files list
      upload_files = request.FILES.getlist('file')

      for upload_file in upload_files:
        # Save the uploaded file to temp dir
        tmp_filename = os.path.join(tempfile.gettempdir(), 'binspdt.' + time.strftime('%Y%m%d%H%M%S', time.localtime()) + '.' + upload_file.name)
        with open(tmp_filename, 'wb') as f:
          for chunk in upload_file.chunks(): 
            f.write(chunk)

        # Import the uploaded idb file
        db.import_idb(tmp_filename, ida_version)

        # Delete the uploaded file from temp dir
        os.remove(tmp_filename)
      return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
      return Response({
        'msg': 'failed to create module',
      }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
