from binary.utils import db
from binary.core.asm import Module

def normalize_api_set_result(analysis):
  module_1 = Module(db=db, module_id=analysis['module_1_id']).load()
  module_2 = Module(db=db, module_id=analysis['module_2_id']).load()

  k = analysis['params']['k']

  matched_functions = analysis['result']['matched_functions']
  overall_similarity = analysis['result']['overall_similarity']

  result = {
    'module_1_birthmark': module_1.api_set_birthmark[k],
    'module_2_birthmark': module_2.api_set_birthmark[k],
    'matched_functions': matched_functions,
    'overall_similarity': overall_similarity,
  }
  return result

def normalize_k_gram_result(analysis):
  module_1 = Module(db=db, module_id=analysis['module_1_id']).load()
  module_2 = Module(db=db, module_id=analysis['module_2_id']).load()

  k = analysis['params']['k']

  similarity_1_to_2 = analysis['result']['similarity_1_to_2']
  similarity_2_to_1 = analysis['result']['similarity_2_to_1']

  module_1_birthmark = module_1.k_gram_birthmark[k]
  module_2_birthmark = module_2.k_gram_birthmark[k]

  intersection = set.intersection(module_1_birthmark, module_2_birthmark)
  module_1_diff = set.difference(module_1_birthmark, intersection)
  module_2_diff = set.difference(module_2_birthmark, intersection)

  result = {
    'intersection': list(intersection),
    'module_1_diff': list(module_1_diff),
    'module_2_diff': list(module_2_diff),
    'module_1_count': len(module_1_birthmark),
    'module_2_count': len(module_2_birthmark),
    'similarity_1_to_2': similarity_1_to_2,
    'similarity_2_to_1': similarity_2_to_1,
  }
  return result

def normalize_api_frequency_result(analysis):
  module_1 = Module(db=db, module_id=analysis['module_1_id']).load()
  module_2 = Module(db=db, module_id=analysis['module_2_id']).load()

  result = {
    'overall_similarity': analysis['result']['overall_similarity'],
    'module_1_birthmark': module_1.api_frequency_birthmark,
    'module_2_birthmark': module_2.api_frequency_birthmark,
  }
  return result

def normalize_key_read_write_result(analysis):
  module_1 = Module(db=db, module_id=analysis['module_1_id']).load()
  module_2 = Module(db=db, module_id=analysis['module_2_id']).load()

  module_1_birthmark = module_1.key_read_write_birthmark
  module_2_birthmark = module_2.key_read_write_birthmark

  k =analysis['params']['k']
  overall_similarity = analysis['result']['overall_similarity']
  module_1_funcs = analysis['result']['module_1_funcs']
  module_2_funcs = analysis['result']['module_2_funcs']
  matched_sequence = analysis['result']['matched_sequence']
  matched_vector = analysis['result']['matched_vector']

  result = {
    'overall_similarity': overall_similarity,
    'module_1_funcs': module_1_funcs,
    'module_2_funcs': module_2_funcs,
    'matched_sequence': matched_sequence,
    'matched_vector': matched_vector,
  }
  return result

def normalize_result(analysis):
  if analysis['method'] == 'api_set':
    return normalize_api_set_result(analysis)
  elif analysis['method'] == 'k_gram':
    return normalize_k_gram_result(analysis)
  elif analysis['method'] == 'api_frequency':
    return normalize_api_frequency_result(analysis)
  elif analysis['method'] == 'key_read_write':
    return normalize_key_read_write_result(analysis)
  else:
    return None
