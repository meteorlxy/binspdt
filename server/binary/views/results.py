from django.core.paginator import Paginator
from binary.utils.decorators import method_allow, api_view
from binary.utils.helpers import model_serializable
from binary.utils import analysis, db, storage
from binary.core.asm import Module
from binary.models import ModuleResult

def normalize_api_result(result_obj):
  module_1 = Module(db=db, module_id=result_obj['module_1_id']).load()
  module_2 = Module(db=db, module_id=result_obj['module_2_id']).load()

  k = result_obj['params']['k']

  sim_matrix = result_obj['details']['sim_matrix']
  match = result_obj['details']['match']

  module_1_api_birthmark = module_1.api_birthmark[k]
  module_2_api_birthmark = module_2.api_birthmark[k]

  module_1_func_addr_list = list(module_1_api_birthmark.keys())
  module_2_func_addr_list = list(module_2_api_birthmark.keys())

  matched_functions = list()
  for x in range(len(match['x'])):
    y = match['x'][x]
    if y == -1:
      break
    module_1_func_addr = module_1_func_addr_list[x]
    module_2_func_addr = module_2_func_addr_list[y]
    functions_pair = {
      'module_1_function_address': module_1_func_addr,
      'module_1_function_api': list(module_1_api_birthmark[module_1_func_addr]),
      'module_2_function_address': module_2_func_addr,
      'module_2_function_api': list(module_2_api_birthmark[module_2_func_addr]),
      'similarity': sim_matrix[x][y]
    }
    matched_functions.append(functions_pair)
  del result_obj['details']['sim_matrix']
  del result_obj['details']['match']
  data = {
    'module_1_details': {
      'id': result_obj['module_1_id'],
      'functions_with_api_count': len(module_1_api_birthmark)
    },
    'module_2_details': {
      'id': result_obj['module_2_id'],
      'functions_with_api_count': len(module_2_api_birthmark)
    },
    'matched_functions': matched_functions,
    'overall_similarity': result_obj['details']['overall_similarity'],
    'params': result_obj['params']
  }
  return data

@method_allow(['GET'])
@api_view()
def index(request):
  page = request.GET.get('page', 1)
  per_page = request.GET.get('perpage', 20)

  results_all = ModuleResult.objects.all().order_by('-id')

  results_pages = Paginator(results_all, per_page)

  results = results_pages.page(page).object_list.values()

  return {
    'data': {
      'data': list(results),
      'count': results_pages.count,
      'num_pages': results_pages.num_pages,
      'page': page,
      'per_page': per_page
    }
  }

@method_allow(['GET', 'DELETE'])
@api_view()
def details(request, result_id):
  """
  Show details of a result or delete a result
  """
  result = ModuleResult.objects.get(id=result_id)
  result_path = result.path
  result_type = result.type

  response = {}
  if request.method == 'GET':
    result_obj = storage.read(result_path)
    if result_type == 'api':
      response['data'] = normalize_api_result(result_obj)
    else:
      response['data'] = result_obj

  if request.method == 'DELETE':
    try:
      analysis.delete(result_path)
    except Exception:
      response['err'] = -1
      response['msg'] = 'fail to delete result'
      response['data'] = {
        'result_id': result_id
      }
  return response