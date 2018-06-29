from .instruction import Instruction
from .operand import Operand

class BasicBlock(object):
  def __init__(
    self,
    parent_module,
    basic_block_dict
  ):
    self._module = parent_module

    self.id = basic_block_dict['id']
    self.parent_function = basic_block_dict['parent_function']
    self.instructions = dict()

    self.has_loaded_instructions = False
    self.has_loaded_operands = False

  def load_instructions(self):
    if (not self.has_loaded_instructions):
      instructions = self._module._db.get_basic_block_instructions(module_id=self._module.id, basic_block_id=self.id)
      self.instructions = dict(
        (
          inst['address'],
          Instruction(
            parent_module=self._module,
            instruction_dict=inst
          )
        ) for inst in instructions
      )

    self.has_loaded_instructions = True
    return self

  def load_operands(self):
    if not self._module.has_loaded_expression_trees:
      self._module.load_expression_trees()
    if not self.has_loaded_operands:
      result_list = self._module._db.get_basic_block_operands(module_id=self._module.id, basic_block_id=self.id)
      for result in result_list:
        if result['address'] not in self.instructions:
          self.instructions[result['address']] = Instruction(
            parent_module=self._module,
            instruction_dict=result
          )
        inst = self.instructions[result['address']]
        if result['op_position'] not in inst.operands:
          op_dict = dict()
          op_dict['address'] = result['op_address']
          op_dict['expression_tree_id'] = result['op_expression_tree_id']
          op_dict['position'] = result['op_position']
          inst.operands[result['op_position']] = Operand(
            parent_module=self._module,
            operand_dict=op_dict
          )
          inst.has_loaded_operands = True
      self.has_loaded_instructions = True
      self.has_loaded_operands = True
    return self

  def __str__(self):
    instructions = ('[%s Instruction in total]' % len(self.instructions)) if self.has_loaded_instructions else None
    return 'BasicBlock: ' + {
      'id': self.id,
      'parent_function': '[address %s]' % self.parent_function,
      'instructions': instructions
    }.__str__()
