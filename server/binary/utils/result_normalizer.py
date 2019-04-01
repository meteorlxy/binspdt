from binary.utils import db
from binary.core.asm import Module

def normalize_api_set_result(analysis):
  module_1 = Module(db=db, module_id=analysis['module_1_id']).load()
  module_2 = Module(db=db, module_id=analysis['module_2_id']).load()

  k = analysis['params']['k']

  sim_matrix = analysis['result']['sim_matrix']
  match = analysis['result']['match']
  overall_similarity = analysis['result']['overall_similarity']

  module_1_api_set_birthmark = module_1.api_set_birthmark[k]
  module_2_api_set_birthmark = module_2.api_set_birthmark[k]

  module_1_func_addr_list = list(module_1_api_set_birthmark.keys())
  module_2_func_addr_list = list(module_2_api_set_birthmark.keys())

  matched_functions = list()
  for x in range(len(match['x'])):
    y = match['x'][x]
    if y == -1:
      break
    module_1_func_addr = module_1_func_addr_list[x]
    module_2_func_addr = module_2_func_addr_list[y]
    functions_pair = {
      'module_1_function_address': module_1_func_addr,
      'module_1_function_api': list(module_1_api_set_birthmark[module_1_func_addr]),
      'module_2_function_address': module_2_func_addr,
      'module_2_function_api': list(module_2_api_set_birthmark[module_2_func_addr]),
      'similarity': sim_matrix[x][y]
    }
    matched_functions.append(functions_pair)
  result = {
    'module_1_functions_with_api_count': len(module_1_api_set_birthmark),
    'module_2_functions_with_api_count': len(module_2_api_set_birthmark),
    'matched_functions': matched_functions,
    'overall_similarity': overall_similarity,
  }
  return result

def normalize_k_gram_result(analysis):
  module_1 = Module(db=db, module_id=analysis['module_1_id']).load()
  module_2 = Module(db=db, module_id=analysis['module_2_id']).load()

  k = analysis['params']['k']

  overall_similarity = analysis['result']['overall_similarity']

  module_1_k_gram_birthmark = module_1.k_gram_birthmark[k]
  module_2_k_gram_birthmark = module_2.k_gram_birthmark[k]

  intersection = set.intersection(module_1_k_gram_birthmark, module_2_k_gram_birthmark)
  module_1_diff = set.difference(module_1_k_gram_birthmark, intersection)
  module_2_diff = set.difference(module_2_k_gram_birthmark, intersection)

  result = {
    'intersection': list(intersection),
    'module_1_diff': list(module_1_diff),
    'module_2_diff': list(module_2_diff),
    'overall_similarity': overall_similarity,
  }
  return result

def normalize_result(analysis):
  if analysis['method'] == 'api_set':
    return normalize_api_set_result(analysis)
  elif analysis['method'] == 'k_gram':
    return normalize_k_gram_result(analysis)
  else:
    return None
