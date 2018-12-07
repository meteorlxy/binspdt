import os
import time
import tempfile

from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from binary.models import Module
from binary.serializers.module import ModuleSerializer
from binary.utils import db

class Modules(ViewSet):
  """
  Handle modules request
  """
  def index(self, request, format='json'):
    """
    Get modules list
    """
    params = {
      'page': request.GET.get('page', 1),
      'per_page': request.GET.get('per_page', 25),
      'order_by': request.GET.get('order_by', 'id'),
    }
    if params['order_by'] not in tuple(field.name for field in Module._meta.get_fields()):
      params['order_by'] = 'id'

    qeuryset = Module.objects.all().order_by(params['order_by'])
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
    # try:
    #   # Delete all related analysis results
    #   results = ModuleResult.objects.filter(Q(module_1_id=module_id) | Q(module_2_id=module_id))
    #   for result in results:
    #     analysis.delete(result.path)
    #   # Delete the module itself
    #   db.delete_module(module_id)
    # except Exception:
    #   response['err'] = -1
    #   response['msg'] = 'fail to delete module'
    #   response['data'] = {
    #     'module_id': module_id
    #   }
    return Response({
      'data': '',
    })
  
  def create(self, ida_version='6.8', format='json'):
    """
    Create a module from uploaded idb file
    """
    try:
      # Get the upload file
      upload_file = request.FILES['file']

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
    except Exception:
      return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
