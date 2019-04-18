import logging
import traceback
import time

from celery import shared_task

from django.db.models import Q
from django.utils import timezone

from binary.utils import db
from binary.models import ModuleAnalysis
from binary.core.analysis import api_set, api_frequency, k_gram, key_read_write

logger = logging.getLogger('binspdt.tasks')

def _start(id):
  analysis = ModuleAnalysis.objects.get(id=id)
  interval = 20
  while True:
    running_analysis = ModuleAnalysis.objects.exclude(
      Q(id__exact=id) | Q(started_at__exact=None),
    ).filter(
      Q(finished_at__exact=None) & Q(failed_at__exact=None),
      Q(module_1_id__exact=analysis.module_1_id) |
      Q(module_2_id__exact=analysis.module_1_id) |
      Q(module_1_id__exact=analysis.module_2_id) |
      Q(module_2_id__exact=analysis.module_2_id),
    )
    if len(running_analysis) > 0:
      logger.info('[task:run_analysis][id:{}] Analysis conflict, wait for {} second'.format(id, interval))
      time.sleep(interval)
    else:
      break

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
      result = api_set.analyse(
        db=db,
        module_1_id=analysis.module_1_id,
        module_2_id=analysis.module_2_id,
        k=analysis.params['k'],
        algorithm=analysis.params['algorithm'],
      )
    elif analysis.method == 'k_gram':
      result = k_gram.analyse(
        db=db,
        module_1_id=analysis.module_1_id,
        module_2_id=analysis.module_2_id,
        k=analysis.params['k'],
      )
    elif analysis.method == 'key_read_write':
      result = key_read_write.analyse(
        db=db,
        module_1_id=analysis.module_1_id,
        module_2_id=analysis.module_2_id,
        k=analysis.params['k'],
        match_sequence=analysis.params['match_sequence'],
        match_vector=analysis.params['match_vector'],
        algorithm=analysis.params['algorithm'],
      )
    elif analysis.method == 'api_frequency': 
      result = api_frequency.analyse(
        db=db,
        module_1_id=analysis.module_1_id,
        module_2_id=analysis.module_2_id,
      )
    else:
      raise Exception('Analysis method is invalid')

    _finish(id, result)

    return True
  except Exception as e:
    _fail(id)
    logger.error(e)
    logger.error(traceback.format_exc())
    return False
  except ModuleAnalysis.DoesNotExist as e:
    logger.info('[task:run_analysis][id:{}] Analysis does not exist'.format(id))
    logger.error(e)
    return False
