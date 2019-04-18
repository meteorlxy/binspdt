import re
import numpy as np
from ..asm import Module
from ..algorithms import KM, jaccard_avg_length

def normalize_api_name(raw_name):
  norm_name = raw_name
  if norm_name.startswith('__imp_'):
    norm_name = norm_name.replace('__imp_', '')
  if norm_name.endswith('_0'):
    norm_name = norm_name.replace('_0', '')
  # E.g. ctime@@GLIBC_2.2.5 => ctime
  match = re.match('^([^@]*)@+.*$', norm_name)
  if match:
    norm_name = match.group(1)
  return norm_name

def load_calls(module):
  if not hasattr(module, 'has_loaded_calls'):
    for func in module.functions.values():
      func.api_calls = set()
      func.function_calls = list()
    for edge in module.callgraph:
      src_func = module.functions[edge['source']]
      dest_func = module.functions[edge['destination']]
      if dest_func.type == 2 or dest_func.type == 3:
        src_func.api_calls.add(normalize_api_name(dest_func.name))
      else:
        src_func.function_calls.append(dest_func)
    module.has_loaded_calls = True

def get_k_depth(f, f_b, k):
  if k < 1:
    return
  for func_call in f.function_calls:
    f_b |= func_call.api_calls
    get_k_depth(f, f_b, k-1)

def generate_birthmark(module, k):
  if not hasattr(module, 'api_set_birthmark'):
    module.api_set_birthmark = dict()
  if k not in module.api_set_birthmark:
    birthmark = dict()
    for func in module.functions.values():
      func_api_set_birthmark = func.api_calls.copy()
      get_k_depth(func, func_api_set_birthmark, k-1)
      if len(func_api_set_birthmark) > 0:
        birthmark[func.address] = func_api_set_birthmark
    module.api_set_birthmark[k] = birthmark

def get_similarity_matrix(module_1, module_2, k):
  if hasattr(module_1, 'api_set_birthmark') and hasattr(module_2, 'api_set_birthmark'):
    if (k in module_1.api_set_birthmark) and (k in module_2.api_set_birthmark):
      sim_matrix = list()
      for mod1 in module_1.api_set_birthmark[k].values():
        mod1_sim = list()
        for mod2 in module_2.api_set_birthmark[k].values():
          mod1_sim.append(jaccard_avg_length(mod1, mod2))
        sim_matrix.append(mod1_sim)
      return sim_matrix
  return False

def run_matching(sim_matrix, algorithm, precision):
  if algorithm == 'km':
    sim_martix_np = np.array(sim_matrix)

    # run KM matching algorithm
    km = KM(sim_martix_np * precision)
    match = km.run()

    # sum up the similarity
    sim_sum = 0
    for x in range(len(match['x'])):
      if match['x'][x] != -1:
        sim_sum += sim_matrix[x][match['x'][x]]

    # calculate similarity with all functions
    similarity = 2 * sim_sum / (len(sim_matrix) + len(sim_matrix[0]))

    return match, similarity
  else:
    print('Matching algorithm invalid')
    return None

def get_matched_functions(module_1_functions, module_2_functions, sim_matrix, match):
  matched_functions = list()
  for x in range(len(match['x'])):
    y = match['x'][x]
    if y == -1:
      continue
    module_1_func_addr = module_1_functions[x]
    module_2_func_addr = module_2_functions[y]
    functions_pair = {
      'module_1_function_address': module_1_func_addr,
      'module_2_function_address': module_2_func_addr,
      'similarity': sim_matrix[x][y],
    }
    matched_functions.append(functions_pair)
  return matched_functions

def analyse(db, module_1_id, module_2_id, k=2, algorithm='km', precision=10000):
  # Generate API Set birthmark
  module_1 = Module(db=db, module_id=module_1_id).load().load_callgraph()
  module_2 = Module(db=db, module_id=module_2_id).load().load_callgraph()

  load_calls(module_1)
  load_calls(module_2)

  generate_birthmark(module_1, k)
  generate_birthmark(module_2, k)

  module_1.save(force=True)
  module_2.save(force=True)

  # Caculating API Set birthmark similarity
  sim_matrix = get_similarity_matrix(module_1, module_2, k)

  match, overall_similarity = run_matching(sim_matrix, algorithm, precision)

  matched_functions = get_matched_functions(
    module_1_functions=list(module_1.api_set_birthmark[k].keys()),
    module_2_functions=list(module_2.api_set_birthmark[k].keys()),
    sim_matrix=sim_matrix,
    match=match,
  )

  # Generating result
  result = {
    'sim_matrix': sim_matrix,
    'matched_functions': matched_functions,
    'overall_similarity': overall_similarity,
  }
  return result
