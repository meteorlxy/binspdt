class Operand(object):
  def __init__(self, parent_module, operand_dict):
    self._module = parent_module

    self.address = operand_dict['address']
    self.position = operand_dict['position']
    self.expression_tree_id = operand_dict['expression_tree_id']

    self.expression_tree = self._module.expression_trees[self.expression_tree_id]

  def display(self):
    pass

  def __str__(self):
    return 'Operand: ' + {
      'address': self.address,
      'position': self.position,
      'expression_tree_id': self.expression_tree_id,
    }.__str__()
