import os
import time
import tempfile
from django.conf import settings
from binary.core.utils import Database
from binary.models import Module
from binary.utils.decorators import method_allow, api_view
from binary.utils.db import db

# from binary.tasks import module_import

def handle_module_upload(upload_file, ida_version):
  tmp_filename = os.path.join(tempfile.gettempdir(), 'binspdt.' + time.strftime('%Y%m%d%H%M%S', time.localtime()) + '.' + upload_file.name)
  with open(tmp_filename, 'wb+') as f:
    for chunk in upload_file.chunks(): 
      f.write(chunk)
  db.import_idb(tmp_filename, ida_version)
  os.remove(tmp_filename)

# Import IDB file
@method_allow(['POST'])
@api_view
def upload(request, ida_version = '6.8'):
  # module_import.delay(request.FILES['file'], ida_version)
  handle_module_upload(request.FILES['file'], ida_version)
  return {}

# Get modules list
@method_allow(['GET'])
@api_view
def index(request):
  return {
    # 'data': list(Module.objects.values())
    'data': db.get_modules()
  }

# Show detail of a module or delete a module
@method_allow(['GET', 'DELETE'])
@api_view
def detail(request, module_id):
  response = {}
  if request.method == 'GET':
    response['data'] = 'module_detail'
  if request.method == 'DELETE':
    response['data'] = db.delete_module(module_id)
  return response

# Show detail of a module or delete a module
@method_allow(['POST'])
@api_view
def load(request, modules_id):
  db.load_module(modules_id)
  return {}