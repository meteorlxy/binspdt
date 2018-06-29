from os import path, makedirs
from django.utils import timezone
from binary.utils import db, storage
from binary.models import ModuleResult

def start(path, type, module_1_id, module_2_id):
  """
  Called before start an analysis, create a record in database
  """
  ModuleResult.objects.create(
    path=path,
    type=type,
    module_1_id=module_1_id,
    module_2_id=module_2_id,
  )
  return True

def finish(path, result):
  """
  Called after finish an analysis, set the finished_at of the analysis record
  """
  try:
    record = ModuleResult.objects.get(path=path)
    if record.finished_at == None:
      storage.write(record.path, result)
      record.finished_at = timezone.now()
      record.save()
    return True
  except Exception:
    return False

def fail(path):
  """
  Called when an analysis is failed, set the failed_at of the analysis record
  """
  try:
    record = ModuleResult.objects.get(path=path)
    if record.failed_at == None:
      record.failed_at = timezone.now()
      record.save()
    return True
  except Exception:
    return False

def delete(path):
  """
  Called to delete an analysis result, delete the record and the pickled file
  """
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
  """
  Called to check the status of an analysis
  """
  try:
    record = ModuleResult.objects.get(path=path)
    if record.failed_at != None:
      return 'failed'
    elif record.finished_at == None:
      return 'pending'
    else:
      return 'done'
  except Exception:
    return 'none'
