import numpy as np
from ..asm import Module
from ..algorithms import KM, lcs, euclidean_norm

value_updating_instructions = (
  # standard mathematical operations
  'adc',
  'add',
  'inc',
  'sub',
  'sbb',
  'dec',
  'div',
  'idiv',
  'mul',
  'imul',
  # logical operations
  'and',
  'or',
  'xor',
  'not',
  # bitshift arithmetic and logical operations
  'sal',
  'sar',
  'shl',
  'shr',
  # bitshift rorate operantions
  'rol',
  'ror',
  'rcl',
  'rcr',
)

def check_mnemonic(mnemonic, mnemonic_tuple):
  for key_word in mnemonic_tuple:
    if key_word in mnemonic:
      return True
  return False

def get_operand_type(operand):
  if operand.type == 'memory':
    return 'MEM'
  elif operand.type == 'register':
    return 'REG'
  else:
    return 'VAL'

def add_to_vector_dict(vector_dict, item):
  if item in vector_dict:
    vector_dict[item] += 1
  else:
    vector_dict[item] = 1

def generate_birthmark(module, k):
  '''
  Example of Key Read-Write birthmark:

  module.key_read_write_birthmark = {
    'read_write_vector': {
      'k': {
        ('add REG,VAL', 'sub REG,MEM'): 1,
      },

      'functions': {
        'FUNCTION_ADDRESS': {
          'read_write_vector': {
            'k': {
              ('add REG,VAL', 'sub REG,MEM'): 1,
            },
          },

          'read_write_sequence': [
            'rREG',
            'rVAL',
            'wREG',
            'rREG',
            'rMEM',
            'wREG',
          ],

          'basic_blocks': {
            'BASIC_BLOCK_ID': {
              'instruction': [
                'add REG,VAL',
                'sub REG,MEM',
              ],

              'read_write': [
                'rREG', 'rVAL', 'wREG',
                'rREG', 'rMEM', 'wREG',
              ],
            },
          },
        },
      },
    },
  }
  '''
  if not hasattr(module, 'key_read_write_birthmark'):
    # generate module birthmark
    module_birthmark = {
      'read_write_vector': dict(),
      'functions': dict(),
    }

    for func in module.functions.values():
      # filter external functions
      if func.type != 0:
        continue
      func_birthmark = {
        'read_write_vector': dict(),
        'read_write_sequence': list(),
        'basic_blocks': dict(),
      }
      # for each basic block
      for bb in func.basic_blocks.values():
        bb_birthmark = {
          'instruction': list(),
          'read_write': list(),
        }

        # for each instruction
        for instruction in bb.instructions.values():
          # filter non-value-updating instructions
          if not check_mnemonic(instruction.mnemonic, value_updating_instructions):
            continue

          # get the mnemonic
          mnemonic = instruction.mnemonic

          # get the abstracted operands
          operands = list()
          for operand in instruction.operands.values():
            operands.append(get_operand_type(operand))

          # get the instruction read-write sequence
          inst_rw_seq = list()
          opreands_count = len(operands)
          if opreands_count == 1:
            inst_rw_seq.append('r%s' % operands[0])
            inst_rw_seq.append('w%s' % operands[0])
          elif opreands_count == 2:
            inst_rw_seq.append('r%s' % operands[0])
            inst_rw_seq.append('r%s' % operands[1])
            inst_rw_seq.append('w%s' % operands[0])
          elif opreands_count == 3:
            inst_rw_seq.append('r%s' % operands[1])
            inst_rw_seq.append('r%s' % operands[2])
            inst_rw_seq.append('w%s' % operands[0])

          # get the instruction symbol
          inst_symbol = '%s %s' % (mnemonic, ','.join(operands))
          # inst_symbol = '%s' % mnemonic

          # generate basic_block birthmark
          bb_birthmark['instruction'].append(inst_symbol)
          bb_birthmark['read_write'] += inst_rw_seq

          # generate function read_write_sequence
          func_birthmark['read_write_sequence'] += inst_rw_seq
        
        # generate function abstraction
        func_birthmark['basic_blocks'][bb.id] = bb_birthmark
      
      # generate module abstraction
      module_birthmark['functions'][func.address] = func_birthmark
    
    # save abstraction to module
    module.key_read_write_birthmark = module_birthmark
  
  if k not in module.key_read_write_birthmark['read_write_vector']:
    # generate module's read_write_vector according to k
    module_read_write_vector = dict()

    for function_address, function in module.key_read_write_birthmark['functions'].items():
      # generate functions's read_write_vector according to k
      function_read_write_vector = dict()

      for basic_block in function['basic_blocks'].values():
        # generate read_write_vector with k
        inst_list = basic_block['instruction']
        if len(inst_list) >= k:
          for i in range(len(inst_list) - k + 1):
            vector_item = tuple(inst_list[i:i + k])
            add_to_vector_dict(module_read_write_vector, vector_item)
            add_to_vector_dict(function_read_write_vector, vector_item)

      # save function birthmark
      function['read_write_vector'][k] = function_read_write_vector

    # save module birthmark
    module.key_read_write_birthmark['read_write_vector'][k] = module_read_write_vector

def get_similarity_matrix(module_1, module_2, k):
  count = 0
  sim_matrix_seq = list()
  sim_matrix_vec = list()
  module_1_funcs = dict()
  module_2_funcs = dict()

  for mod1_func_addr, mod1_func in module_1.key_read_write_birthmark['functions'].items():
    sim_line_seq = list()
    sim_line_vec = list()
    mod1_func_seq = mod1_func['read_write_sequence']
    mod1_func_vec = mod1_func['read_write_vector'][k]
    for mod2_func_addr, mod2_func in module_2.key_read_write_birthmark['functions'].items():
      mod2_func_seq = mod2_func['read_write_sequence']
      mod2_func_vec = mod2_func['read_write_vector'][k]

      # calculate sequence similarity
      sim_seq = 0
      avg_len = (len(mod1_func_seq) + len(mod2_func_seq)) / 2
      # max_len = max([len(mod1_func_seq), len(mod2_func_seq)])
      if avg_len > 3 * k:
        sim_seq = lcs(mod1_func_seq, mod2_func_seq, exact=True) / avg_len
      sim_line_seq.append(sim_seq)

      # calculate vector similarity
      sim_vec = euclidean_norm(mod1_func_vec, mod2_func_vec)
      sim_line_vec.append(sim_vec)

      if mod1_func_addr not in module_1_funcs:
        module_1_funcs[mod1_func_addr] = dict()

      if mod2_func_addr not in module_1_funcs[mod1_func_addr]:
        module_1_funcs[mod1_func_addr][mod2_func_addr] = {
          'similarity_sequence': sim_seq,
          'similarity_vector': sim_vec,
        }

      if mod2_func_addr not in module_2_funcs:
        module_2_funcs[mod2_func_addr] = dict()

      if mod1_func_addr not in module_2_funcs[mod2_func_addr]:
        module_2_funcs[mod2_func_addr][mod1_func_addr] = {
          'similarity_sequence': sim_seq,
          'similarity_vector': sim_vec,
        }

    sim_matrix_seq.append(sim_line_seq)
    sim_matrix_vec.append(sim_line_vec)
  return sim_matrix_seq, sim_matrix_vec, module_1_funcs, module_2_funcs

def run_matching(sim_matrix, algorithm, precision):
  if algorithm == 'km':
    sim_martix_np = np.array(sim_matrix)

    # run KM matching algorithm
    km = KM(sim_martix_np * precision)
    match = km.run()

    # sum up the similarity
    sim_sum = 0
    len_x = 0
    len_y = 0
    for x in range(len(match['x'])):
      if match['x'][x] != -1:
        sim_sum += sim_matrix[x][match['x'][x]]
      # filter all-zero lines
      if max(sim_martix_np[x]) > 0:
        len_x += 1
    for y in range(len(match['y'])):
      # filter all-zero columns
      if max(sim_martix_np[:, y]) > 0:
        len_y += 1

    # calculate similarity with all functions
    similarity = 2 * sim_sum / (len(sim_matrix) + len(sim_matrix[0]))

    # calculate similarity with non-zero functions
    similarity_filtered = 0 if len_x + len_y == 0 else 2 * sim_sum / (len_x + len_y)

    similarity_x_to_y = sim_sum / len(sim_matrix[0])
    similarity_x_to_y_filtered = 0 if len_y == 0 else sim_sum / len_y
    similarity_y_to_x = sim_sum / len(sim_matrix)
    similarity_y_to_x_filtered = 0 if len_x == 0 else sim_sum / len_x

    return match, similarity, similarity_filtered, similarity_x_to_y, similarity_x_to_y_filtered, similarity_y_to_x, similarity_y_to_x_filtered
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

def analyse(db, module_1_id, module_2_id, k, match_sequence=False, match_vector=False, algorithm='km', precision=10000, generate_matrix=True):
  # Generate Key Read-Write birthmark
  module_1 = Module(db=db, module_id=module_1_id).load().load_operands()
  module_2 = Module(db=db, module_id=module_2_id).load().load_operands()

  generate_birthmark(module_1, k)
  generate_birthmark(module_2, k)

  module_1.save(force=True)
  module_2.save(force=True)

  # Caculateg Key Read-Write birthmark similarity
  sim_euclidean = euclidean_norm(
    module_1.key_read_write_birthmark['read_write_vector'][k],
    module_2.key_read_write_birthmark['read_write_vector'][k],
  )

  sim_matrix_seq, sim_matrix_vec, module_1_funcs, module_2_funcs = None, None, None, None
  if generate_matrix:
    sim_matrix_seq, sim_matrix_vec, module_1_funcs, module_2_funcs = get_similarity_matrix(module_1, module_2, k)

  matched_sequence = None
  if generate_matrix and match_sequence:
    match_seq, similarity_seq, similarity_filtered_seq, similarity_1_to_2_seq, similarity_1_to_2_filtered_seq, similarity_2_to_1_seq, similarity_2_to_1_filtered_seq = run_matching(sim_matrix_seq, algorithm, precision)
    matched_functions_seq = get_matched_functions(
      module_1_functions=list(module_1.key_read_write_birthmark['functions'].keys()),
      module_2_functions=list(module_2.key_read_write_birthmark['functions'].keys()),
      sim_matrix=sim_matrix_seq,
      match=match_seq,
    )
    matched_sequence = {
      'similarity': similarity_seq,
      'similarity_filtered': similarity_filtered_seq,
      'similarity_1_to_2': similarity_1_to_2_seq,
      'similarity_1_to_2_filtered': similarity_1_to_2_filtered_seq,
      'similarity_2_to_1': similarity_2_to_1_seq,
      'similarity_2_to_1_filtered': similarity_2_to_1_filtered_seq,
      'matched_functions': matched_functions_seq,
    }

  matched_vector = None
  if generate_matrix and match_vector:
    match_vec, similarity_vec, similarity_filtered_vec, similarity_1_to_2_vec, similarity_1_to_2_filtered_vec, similarity_2_to_1_vec, similarity_2_to_1_filtered_vec = run_matching(sim_matrix_vec, algorithm, precision)
    matched_functions_vec = get_matched_functions(
      module_1_functions=list(module_1.key_read_write_birthmark['functions'].keys()),
      module_2_functions=list(module_2.key_read_write_birthmark['functions'].keys()),
      sim_matrix=sim_matrix_vec,
      match=match_vec,
    )
    matched_vector = {
      'similarity': similarity_vec,
      'similarity_filtered': similarity_filtered_vec,
      'similarity_1_to_2': similarity_1_to_2_vec,
      'similarity_1_to_2_filtered': similarity_1_to_2_filtered_vec,
      'similarity_2_to_1': similarity_2_to_1_vec,
      'similarity_2_to_1_filtered': similarity_2_to_1_filtered_vec,
      'matched_functions': matched_functions_vec,
    }

  # Generate result
  return {
    'overall_similarity': sim_euclidean,
    'module_1_funcs': module_1_funcs,
    'module_2_funcs': module_2_funcs,
    'matched_sequence': matched_sequence,
    'matched_vector': matched_vector,
  }
