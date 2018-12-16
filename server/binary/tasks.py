import logging

from celery import shared_task

from django.utils import timezone

from binary.utils import db
from binary.models import ModuleAnalysis
from binary.core.analysis.api import analyse_api

logger = logging.getLogger('binspdt.tasks')

def _start(id):
  analysis = ModuleAnalysis.objects.get(id=id)
  if analysis.started_at == None:
    analysis.started_at = timezone.now()
    analysis.save()
    logger.info('[task:run_analysis][id:{}] Analysis started'.format(id))

def _finish(id, data):
  analysis = ModuleAnalysis.objects.get(id=id)
  if analysis.started_at == None:
    analysis.data = data
    analysis.finished_at = timezone.now()
    analysis.save()
    logger.info('[task:run_analysis][id:{}] Analysis finished'.format(id))

def _fail(id):
  analysis = ModuleAnalysis.objects.get(id=id)
  if analysis.failed_at == None:
    analysis.failed_at = timezone.now()
    analysis.save()
    logger.info('[task:run_analysis][id:{}] Analysis failed'.format(id))

@shared_task
def run_analysis(id):
  try:
    _start(id)

    result = analyse_api(
      db=db,
      module_1_id=analysis.module_1_id,
      module_2_id=analysis.module_2_id,
      k=analysis.params['k'],
      algorithm=analysis.params['algorithm'],
    )

    _finish(id, result)

    return True
  except Exception as e:
    _fail(id)
    logger.error(e)
    return False
  except ModuleAnalysis.DoesNotExist as e:
    logger.info('[task:run_analysis][id:{}] Analysis does not exist'.format(id))
    logger.error(e)
    return False

