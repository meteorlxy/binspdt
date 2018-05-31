from .operand import Operand

class Instruction(object):
  def __init__(self, parent_module, instruction_dict):
    self._module = parent_module

    self.address = instruction_dict['address']
    self.mnemonic = instruction_dict['mnemonic']
    self.operands = dict()

    self.has_loaded_operands = False

  def load_operands(self):
    if not self._module.has_loaded_expression_trees:
      self._module.load_expression_trees()
    if not self.has_loaded_operands:
      operands = self._module._db.get_instruction_operands(module_id=self._module.id, instruction_address=self.address)
      self.operands = dict(
        (
          op['position'],
          Operand(
            parent_module=self._module,
            operand_dict=op
          )
        ) for op in operands
      )
      self.has_loaded_operands = True
    return self

  def __str__(self):
    operands = ('[%s Operand in total]' % len(self.operands)) if self.has_loaded_operands else None    
    return 'Instruction: ' + {
      'address': self.address,
      'mnemonic': self.mnemonic,
      'operands': operands,
    }.__str__()
