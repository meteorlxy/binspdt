from os import path
from binary.utils import analysis
from binary.utils.decorators import method_allow, api_view
from binary.tasks import analyse_api

RESULT_DIR = 'api_result'

def gen_analysis_path(module_1_id, module_2_id, params):
  analysis_key = 'api_module_%(module_1_id)s_module_%(module_2_id)s_k_%(k)s_%(algorithm)s' % {
    'module_1_id': min(module_1_id, module_2_id),
    'module_2_id': max(module_1_id, module_2_id),
    'k': params['k'],
    'algorithm': params['algorithm']
  }
  analysis_path = path.join(RESULT_DIR, analysis_key)
  return analysis_path

def gen_module_detail(module_id, k):
  module = Module(db, module_id).load()
  return {
    'id': module.id,
    'func_num': len(module.functions),
    'func_with_api_num': len(module.api_birthmark[k]),
    'api_birthmark': dict((addr, list(bm)) for (addr, bm) in module.api_birthmark[k].items())
  }

@method_allow(['POST'])
@api_view()
def index(request):
  module_1_id = request.json['module_1']
  module_2_id = request.json['module_2']
  params = {
    'k': request.json['k'],
    'algorithm': request.json['algorithm']
  }

  # Get the identifier of the analysis
  analysis_path = gen_analysis_path(module_1_id=module_1_id, module_2_id=module_2_id, params=params)

  # Check the analysis status
  status = analysis.check_status(path=analysis_path)

  if status == 'done':
    return {
      'err': 0,
      'msg': 'done'
    }
  
  if status == 'pending':
    return {
      'err': 1,
      'msg':'pending'
    }

  # Deliver the analysis task
  analyse_api.delay(
    params=params,
    path=analysis_path,
    type='api',
    module_1_id=module_1_id,
    module_2_id=module_2_id
  )

  return {
    'err': 2,
    'msg': 'start'
  }
