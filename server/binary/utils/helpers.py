from binary.utils import db
from binary.core.asm import Module

def normalize_api_result(result_dict):
  module_1 = Module(db=db, module_id=result_dict['module_1_id']).load()
  module_2 = Module(db=db, module_id=result_dict['module_2_id']).load()

  k = result_dict['params']['k']

  sim_matrix = result_dict['details']['sim_matrix']
  match = result_dict['details']['match']

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
  del result_dict['details']['sim_matrix']
  del result_dict['details']['match']
  data = {
    'module_1_details': {
      'id': result_dict['module_1_id'],
      'functions_with_api_count': len(module_1_api_birthmark)
    },
    'module_2_details': {
      'id': result_dict['module_2_id'],
      'functions_with_api_count': len(module_2_api_birthmark)
    },
    'matched_functions': matched_functions,
    'overall_similarity': result_dict['details']['overall_similarity'],
    'params': result_dict['params']
  }
  return data