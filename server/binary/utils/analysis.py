from os import path, makedirs
from django.utils import timezone
from binary.utils import db, storage
from binary.models import ModuleResult

def start(path, type, module_1_id, module_2_id):
  ModuleResult.objects.create(
    path=path,
    type=type,
    module_1_id=module_1_id,
    module_2_id=module_2_id,
  )
  return True

def finish(path, result):
  try:
    record = ModuleResult.objects.get(path=path)
    if record.finished_at == None:
      storage.write(record.path, result)
      record.finished_at = timezone.now()
      record.save()
    return True
  except Exception:
    return False

def delete(path):
  try:
    record = ModuleResult.objects.get(path=path)
    if record.finished_at == None:
      return False
    storage.delete(record.path)
    record.delete()
    return True
  except Exception:
    return False

def check_status(path):
  try:
    record = ModuleResult.objects.get(path=path)
    if record.finished_at == None:
      return 'pending'
    else:
      return 'done'
  except Exception:
    return 'none'
