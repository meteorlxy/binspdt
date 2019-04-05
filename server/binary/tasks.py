import logging

from celery import shared_task

from django.utils import timezone

from binary.utils import db
from binary.models import ModuleAnalysis
from binary.core.analysis.api_set import analyse_api_set
from binary.core.analysis.k_gram import analyse_k_gram

logger = logging.getLogger('binspdt.tasks')

def _start(id):
  analysis = ModuleAnalysis.objects.get(id=id)
  if analysis.started_at == None:
    analysis.started_at = timezone.now()
    analysis.save()
    logger.info('[task:run_analysis][id:{}] Analysis started'.format(id))

def _finish(id, result):
  analysis = ModuleAnalysis.objects.get(id=id)
  if analysis.finished_at == None:
    analysis.result = result
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

    analysis = ModuleAnalysis.objects.get(id=id)

    result = None

    if analysis.method == 'api_set':
      result = analyse_api_set(
        db=db,
        module_1_id=analysis.module_1_id,
        module_2_id=analysis.module_2_id,
        k=analysis.params['k'],
        algorithm=analysis.params['algorithm'],
      )
    elif analysis.method == 'k_gram':
      result = analyse_k_gram(
        db=db,
        module_1_id=analysis.module_1_id,
        module_2_id=analysis.module_2_id,
        k=analysis.params['k'],
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

