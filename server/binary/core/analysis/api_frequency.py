import re
from collections import deque
from ..asm import Module
from ..algorithms import cosine

def bfs(graph, start_node, target_nodes):
  search_queue = deque(graph[start_node])
  searched_nodes = set()
  result = set()
  while search_queue:
    node = search_queue.popleft()
    if not node in searched_nodes:
      searched_nodes.add(node)
      if node in target_nodes:
        result.add(node)
      else:
        search_queue += graph[node]
  return result

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

def generate_birthmark(module):
  if not hasattr(module, 'api_frequency_birthmark'):
    callgraph = module.callgraph
    functions = module.functions

    module_functions = set()
    external_functions = set()

    for func in functions.values():
      if func.type == 0:
        module_functions.add(func.address)
      else:
        external_functions.add(func.address)

    reversed_graph = dict()
    starting_nodes = module_functions.copy()

    for edge in callgraph:
      if edge['destination'] in reversed_graph:
        reversed_graph[edge['destination']].add(edge['source'])
      else:
        reversed_graph[edge['destination']] = {edge['source']}

      if edge['destination'] in starting_nodes:
        starting_nodes.remove(edge['destination'])

    birthmark = dict()
    for api_func in external_functions:
      freq = 0
      if api_func in reversed_graph:
        freq = len(bfs(reversed_graph, api_func, starting_nodes))
      birthmark[normalize_api_name(functions[api_func].name)] = freq

    module.api_frequency_birthmark = birthmark

def analyse(db, module_1_id, module_2_id):
  # Generate api-frequency birthmark
  module_1 = Module(db=db, module_id=module_1_id).load().load_callgraph()
  module_2 = Module(db=db, module_id=module_2_id).load().load_callgraph()

  generate_birthmark(module_1)
  generate_birthmark(module_2)

  module_1.save(force=True)
  module_2.save(force=True)

  # Caculateg api-frequency birthmark similarity
  overall_similarity = cosine(
    module_1.api_frequency_birthmark,
    module_2.api_frequency_birthmark,
  )

  return {
    'overall_similarity': overall_similarity,
  }