import os
import time
import tempfile
from binary.utils.db import db
from celery import shared_task

@shared_task
def module_import(upload_file, ida_version):
  tmp_filename = os.path.join(tempfile.gettempdir(), 'binspdt.' + time.strftime('%Y%m%d%H%M%S', time.localtime()) + '.' + upload_file.name)
  with open(tmp_filename, 'wb+') as f:
    for chunk in upload_file.chunks(): 
      f.write(chunk)
  db.import_idb(tmp_filename, ida_version)
  os.remove(tmp_filename)
