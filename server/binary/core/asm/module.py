from .function import Function
from .basicblock import BasicBlock
from .instruction import Instruction
from .operand import Operand

class Module(object):
  def __init__(self, db, module_id):
    self._db = db
    self.id = module_id

    self.functions = dict()
    self.callgraph = list()

    self.expression_trees = dict()

    self.has_loaded_module = False
    self.has_loaded_module_details = False
    self.has_loaded_functions = False
    self.has_loaded_basic_blocks = False
    self.has_loaded_instructions = False
    self.has_loaded_operands = False
    self.has_loaded_expression_trees = False
    self.has_loaded_callgraph = False
    self.has_loaded_control_flow_graph = False

    self.load_module()
  
  def load_module(self):
    if not self.has_loaded_module:
      module = self._db.get_module(module_id=self.id)
      if module == None:
        raise Exception('Module {} not found'.format(self.id))
      self.name = module['name']
      self.architecture = module['architecture']
      self.base_address = module['base_address']
      self.exporter = module['exporter']
      self.version = module['version']
      self.md5 = module['md5']
      self.sha1 = module['sha1']
      self.comment = module['comment']
      self.import_time = module['import_time'].strftime("%Y-%m-%d %H:%M:%S")

      self.has_loaded_module = True
    return self
  
  def load_module_details(self):
    if not self.has_loaded_module_details:
      module_details = self._db.get_module_details(module_id=self.id)
      
      self.functions_count = module_details['functions_count']
      self.basic_blocks_count = module_details['basic_blocks_count']
      self.instructions_count = module_details['instructions_count']

      self.has_loaded_module_details = True
    return self

  def load_functions(self):
    if (not self.has_loaded_functions):
      functions = self._db.get_module_functions(module_id=self.id)
      self.functions = dict(
        (
          func['address'],
          Function(
            parent_module=self,
            function_dict=func
          )
        ) for func in functions
      )
    self.has_loaded_functions = True
    return self

  def load_basic_blocks(self):
    if not self.has_loaded_basic_blocks:
      result_list = self._db.get_module_basic_blocks(module_id=self.id)
      for result in result_list:
        if result['address'] not in self.functions:
          self.functions[result['address']] = Function(
            parent_module=self,
            function_dict=result,
          )
        func = self.functions[result['address']]
        if result['bb_id'] not in func.basic_blocks:
          bb_dict = dict()
          bb_dict['id'] = result['bb_id']
          bb_dict['address'] = result['bb_address']
          bb_dict['parent_function'] = result['bb_parent_function']
          func.basic_blocks[result['bb_id']] = BasicBlock(
            parent_module=self,
            basic_block_dict=bb_dict
          )
          func.has_loaded_basic_blocks = True
      self.has_loaded_functions = True
      self.has_loaded_basic_blocks = True
    return self

  def load_instructions(self):
    if not self.has_loaded_instructions:
      result_list = self._db.get_module_instructions(module_id=self.id)
      for result in result_list:
        if result['address'] not in self.functions:
          self.functions[result['address']] = Function(
            parent_module=self,
            function_dict=result,
          )
        func = self.functions[result['address']]
        if result['bb_id'] not in func.basic_blocks:
          bb_dict = dict()
          bb_dict['id'] = result['bb_id']
          bb_dict['address'] = result['bb_address']
          bb_dict['parent_function'] = result['bb_parent_function']
          func.basic_blocks[result['bb_id']] = BasicBlock(
            parent_module=self,
            basic_block_dict=bb_dict
          )
          func.has_loaded_basic_blocks = True
          func.has_loaded_instructions = True
        bb = func.basic_blocks[result['bb_id']]
        if result['inst_address'] not in bb.instructions:
          inst_dict = dict()
          inst_dict['address'] = result['inst_address']
          inst_dict['mnemonic'] = result['inst_mnemonic']
          bb.instructions[result['inst_address']] = Instruction(
            parent_module=self,
            instruction_dict=inst_dict
          )
          bb.has_loaded_instructions = True
      self.has_loaded_functions = True
      self.has_loaded_basic_blocks = True
      self.has_loaded_instructions = True
    return self

  def load_operands(self):
    if not self.has_loaded_expression_trees:
      self.load_expression_trees()
    if not self.has_loaded_operands:
      result_list = self._db.get_module_operands(module_id=self.id)
      for result in result_list:
        if result['address'] not in self.functions:
          self.functions[result['address']] = Function(
            parent_module=self,
            function_dict=result,
          )
        func = self.functions[result['address']]
        if result['bb_id'] not in func.basic_blocks:
          bb_dict = dict()
          bb_dict['id'] = result['bb_id']
          bb_dict['address'] = result['bb_address']
          bb_dict['parent_function'] = result['bb_parent_function']
          func.basic_blocks[result['bb_id']] = BasicBlock(
            parent_module=self,
            basic_block_dict=bb_dict
          )
          func.has_loaded_basic_blocks = True
          func.has_loaded_instructions = True
          func.has_loaded_operands = True
        bb = func.basic_blocks[result['bb_id']]
        if result['inst_address'] not in bb.instructions:
          inst_dict = dict()
          inst_dict['address'] = result['inst_address']
          inst_dict['mnemonic'] = result['inst_mnemonic']
          bb.instructions[result['inst_address']] = Instruction(
            parent_module=self,
            instruction_dict=inst_dict
          )
          bb.has_loaded_instructions = True
          bb.has_loaded_operands = True
        inst = bb.instructions[result['inst_address']]
        if result['op_position'] not in inst.operands:
          op_dict = dict()
          op_dict['address'] = result['op_address']
          op_dict['expression_tree_id'] = result['op_expression_tree_id']
          op_dict['position'] = result['op_position']
          inst.operands[result['op_position']] = Operand(
            parent_module=self,
            operand_dict=op_dict
          )
      self.has_loaded_functions = True
      self.has_loaded_basic_blocks = True
      self.has_loaded_instructions = True
      self.has_loaded_operands = True
    return self
  
  def load_expression_trees(self):
    if not self.has_loaded_expression_trees:
      result_list = self._db.get_module_expression_trees(module_id=self.id)
      for result in result_list:
        if result['tree_id'] not in self.expression_trees:
          self.expression_trees[result['tree_id']] = dict()
        expression_node = result.copy()
        del expression_node['tree_id']
        self.expression_trees[result['tree_id']][expression_node['id']] = expression_node
      self.has_loaded_expression_trees = True
    return self

  def load_callgraph(self):
    if not self.has_loaded_functions:
      self.load_functions()
    if not self.has_loaded_callgraph:
      self.callgraph = self._db.get_callgraph(module_id=self.id)
      self.has_loaded_callgraph = True
    return self

  def save(self, force=False):
    self._db.save_module(self.id, self, force=force)
    return self

  def load(self):
    obj = self._db.load_module(self.id)
    if obj != None:
      self.__dict__.update(obj.__dict__)
    return self

  def __str__(self):
    functions = ('[%s Function in total]' % len(self.functions)) if self.has_loaded_functions else None
    callgraph = ('[%s nodes and %s edges in total]' % (len(self.functions), len(self.callgraph))) if self.has_loaded_callgraph else None
    return 'Module: ' + {
      'id': self.id,
      'name': self.name,
      'architecture': self.architecture,
      'base_address': self.base_address,
      'exporter': self.exporter,
      'version': self.version,
      'md5': self.md5,
      'sha1': self.sha1,
      'comment': self.comment,
      'import_time': self.import_time,
      'functions': functions,
      'callgraph': callgraph
    }.__str__()
  
  def __getstate__(self):
    state = self.__dict__.copy()
    if '_db' in state:
      del state['_db']
    return state
  
  def __setstate__(self, state):
    self.__dict__.update(state)
