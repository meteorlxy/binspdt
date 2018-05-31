from .basicblock import BasicBlock
from .instruction import Instruction
from .operand import Operand

class Function(object):
  def __init__(
    self,
    parent_module,
    function_dict
  ):
    self._module = parent_module

    self.address = function_dict['address']
    self.name = function_dict['name']
    self.demangled_name = function_dict['demangled_name']
    self.has_real_name = function_dict['has_real_name']
    self.type = function_dict['type']
    self.module_name = function_dict['module_name']
    self.stack_frame = function_dict['stack_frame']
    self.prototype = function_dict['prototype']
    self.basic_blocks = dict()
    self.control_flow_graph = list()

    self.has_loaded_basic_blocks = False
    self.has_loaded_instructions = False
    self.has_loaded_operands = False
    self.has_loaded_control_flow_graph = False

  def load_basic_blocks(self):
    if not self.has_loaded_basic_blocks:
      basic_blocks = self._module._db.get_function_basic_blocks(module_id=self._module.id, function_address=self.address)
      self.basic_blocks = dict(
        (
          bb['id'],
          BasicBlock(
            parent_module=self._module,
            basic_block_dict=bb
          )
        ) for bb in basic_blocks
      )
    self.has_loaded_basic_blocks = True
    return self

  def load_instructions(self):
    if not self.has_loaded_instructions:
      result_list = self._module._db.get_function_instructions(module_id=self._module.id, function_address=self.address)
      for result in result_list:
        if result['id'] not in self.basic_blocks:
          self.basic_blocks[result['id']] = BasicBlock(
            parent_module=self._module,
            basic_block_dict=result,
          )
        bb = self.basic_blocks[result['id']]
        if result['inst_address'] not in bb.instructions:
          inst_dict = dict()
          inst_dict['address'] = result['inst_address']
          inst_dict['mnemonic'] = result['inst_mnemonic']
          bb.instructions[result['inst_address']] = Instruction(
            parent_module=self._module,
            instruction_dict=inst_dict
          )
          bb.has_loaded_instructions = True
      self.has_loaded_basic_blocks = True
      self.has_loaded_instructions = True
    return self

  def load_operands(self):
    if not self._module.has_loaded_expression_trees:
      self._module.load_expression_trees()
    if not self.has_loaded_operands:
      result_list = self._module._db.get_function_operands(module_id=self._module.id, function_address=self.address)
      for result in result_list:
        if result['id'] not in self.basic_blocks:
          self.basic_blocks[result['id']] = BasicBlock(
            parent_module=self._module,
            basic_block_dict=result
          )
        bb = self.basic_blocks[result['id']]
        if result['inst_address'] not in bb.instructions:
          inst_dict = dict()
          inst_dict['address'] = result['inst_address']
          inst_dict['mnemonic'] = result['inst_mnemonic']
          bb.instructions[result['inst_address']] = Instruction(
            parent_module=self._module,
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
            parent_module=self._module,
            operand_dict=op_dict
          )
      self.has_loaded_basic_blocks = True
      self.has_loaded_instructions = True
      self.has_loaded_operands = True
    return self

  def load_control_flow_graph(self):
    if not self.has_loaded_basic_blocks:
      self.load_basic_blocks()
    if not self.has_loaded_control_flow_graph:
      self.control_flow_graph = self._module._db.get_control_flow_graph(module_id=self._module.id, function_address=self.address)
      self.has_loaded_control_flow_graph = True
    return self

  def __str__(self):
    basic_blocks = ('[%s BasicBlock in total]' % len(self.basic_blocks)) if self.has_loaded_basic_blocks else None
    control_flow_graph = ('[%s nodes and %s edges in total]' % (len(self.basic_blocks), len(self.control_flow_graph))) if self.has_loaded_control_flow_graph else None
    return 'Function: ' + {
      'address': self.address,
      'name': self.name,
      'demangled_name': self.demangled_name,
      'has_real_name': self.has_real_name,
      'type': self.type,
      'module_name': self.module_name,
      'stack_frame': self.stack_frame,
      'prototype': self.prototype,
      'basic_blocks': basic_blocks,
      'control_flow_graph': control_flow_graph
    }.__str__()
