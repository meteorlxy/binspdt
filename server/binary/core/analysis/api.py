import numpy as np
from ..asm import Module
from ..algorithms import KM

def normalize_api_name(raw_name):
  norm_name = raw_name
  if norm_name.startswith('__imp_'):
    norm_name = norm_name.replace('__imp_', '')
  if norm_name.endswith('_0'):
    norm_name = norm_name.replace('_0', '')
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

def generate_api_birthmark(module, k):
  if not hasattr(module, 'api_birthmark'):
    module.api_birthmark = dict()
  if k not in module.api_birthmark:
    module.api_birthmark[k] = dict()
    for func in module.functions.values():
      func_api_birthmark = func.api_calls.copy()
      get_k_depth(func, func_api_birthmark, k-1)
      if len(func_api_birthmark) > 0:
        module.api_birthmark[k][func.address] = func_api_birthmark

def jaccard_sim(set_1, set_2):
  union = set_1 | set_2
  intersection = set_1 & set_2
  if len(union) == 0 or len(intersection) == 0:
    return 0
  return len(intersection) / len(union)

def modified_jaccard_sim(set_1, set_2):
  intersection = set_1 & set_2
  if len(intersection) == 0:
    return 0
  return 2 * len(intersection) / (len(set_1) + len(set_2))

def get_similarity_matrix(module_1, module_2, k):
  if hasattr(module_1, 'api_birthmark') and hasattr(module_2, 'api_birthmark'):
    if (k in module_1.api_birthmark) and (k in module_2.api_birthmark):
      sim_matrix = list()
      for mod1 in module_1.api_birthmark[k].values():
        mod1_sim = list()
        for mod2 in module_2.api_birthmark[k].values():
          mod1_sim.append(modified_jaccard_sim(mod1, mod2))
        sim_matrix.append(mod1_sim)
      return sim_matrix
  return False

def analyse_api(db, module_1_id, module_2_id, k=2, algorithm='km', precision=1000):
  print('Generating API birthmark...')
  module_1 = Module(db=db, module_id=module_1_id).load().load_callgraph()
  module_2 = Module(db=db, module_id=module_2_id).load().load_callgraph()

  load_calls(module_1)
  load_calls(module_2)

  generate_api_birthmark(module_1, k)
  generate_api_birthmark(module_2, k)

  module_1.save(force=True)
  module_2.save(force=True)

  print('Caculating API birthmark similarity matrix...')
  sim_matrix = get_similarity_matrix(module_1, module_2, k)

  print('Running KM algorithm...')
  km = KM(np.array(sim_matrix) * precision)
  match = km.run()

  print('Generating result...')
  sim_temp = 0
  for x in range(len(match['x'])):
    if match['x'][x] != -1:
      sim_temp += sim_matrix[x][match['x'][x]]
  overall_similarity = 2 * sim_temp / (len(sim_matrix) + len(sim_matrix[0]))

  result = {
    'module_1_id': module_1.id,
    'module_2_id': module_2.id,
    'params': {
      'k': k,
      'algorithm': algorithm,
      'precision': precision
    },
    'details': {
      'sim_matrix': sim_matrix,
      'match': match,
      'overall_similarity': overall_similarity
    }
  }
  return result
