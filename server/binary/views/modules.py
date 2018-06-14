import os
import time
import tempfile
from binary.utils.db import db
from binary.utils.decorators import method_allow, api_view
from binary.core.asm import module

def handle_module_upload(upload_file, ida_version):
  tmp_filename = os.path.join(tempfile.gettempdir(), 'binspdt.' + time.strftime('%Y%m%d%H%M%S', time.localtime()) + '.' + upload_file.name)
  with open(tmp_filename, 'wb') as f:
    for chunk in upload_file.chunks(): 
      f.write(chunk)
  db.import_idb(tmp_filename, ida_version)
  os.remove(tmp_filename)

@method_allow(['POST'])
@api_view(request_json=False)
def upload(request, ida_version = '6.8'):
  """
  Import IDB file
  """
  handle_module_upload(request.FILES['file'], ida_version)
  return {}

@method_allow(['GET'])
@api_view()
def index(request):
  """
  Get modules list
  """
  return {
    'data': db.get_modules()
  }

@method_allow(['GET', 'DELETE'])
@api_view()
def details(request, module_id):
  """
  Show details of a module or delete a module
  """
  response = {}
  if request.method == 'GET':
    module
    response['data'] = db.get_module_details(module_id)
  if request.method == 'DELETE':
    response['data'] = db.delete_module(module_id)
  return response
