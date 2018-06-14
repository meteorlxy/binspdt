import os
from celery import shared_task
from binary.utils import db, analysis
from binary.core.analysis.api import analyse_api as api

@shared_task
def module_import(tmp_filename, ida_version):
  db.import_idb(tmp_filename, ida_version)
  os.remove(tmp_filename)

@shared_task
def analyse_api(params, path, type, module_1_id, module_2_id):
  # Check the analysis status
  status = analysis.check_status(path)

  if status == 'done':
    return True
  
  if status == 'pending':
    return False

  # Run the analysis
  analysis.start(
    path=path,
    type=type,
    module_1_id=module_1_id,
    module_2_id=module_2_id
  )

  result = api(
    db=db,
    module_1_id=module_1_id,
    module_2_id=module_2_id,
    k=params['k'],
    algorithm=params['algorithm']
  )

  analysis.finish(path=path, result=result)

  return True

