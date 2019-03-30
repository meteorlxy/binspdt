"""
Expression Tree

- type
  - 1 Unknown
  - 2 Immediate Value
  - 3 Unknown
  - 4 Memery Related Operator (+, *, ds:, ss:, fs: ...)
  - 5 Register (ebx, esp ...)
  - 6 Data Type (b1, b2, b4 ...)
  - 7 Square brackets ([)

- parent_id
  ID of parent expression_node

- position
  Position of nodes that has the same parent_id
"""


class Operand(object):
  def __init__(self, parent_module, operand_dict):
    self._module = parent_module

    self.address = operand_dict['address']
    self.position = operand_dict['position']
    self.expression_tree_id = operand_dict['expression_tree_id']

    self.expression_tree = self._module.expression_trees[self.expression_tree_id]

    self.type = None
    self.data_type = None
    self.symbol = None
    self.__parse()
  
  def __parse(self):
    exp_tree = self._module.expression_trees[self.expression_tree_id]
    exp_tree_nodes = list(exp_tree.values())
    self.data_type = exp_tree_nodes[0]['symbol']
    if len(exp_tree) == 2:
      symbol_node = exp_tree_nodes[1]
      if symbol_node['type'] == 2:
        self.type = 'immediate value'
      else:
        self.type = 'register'
      self.symbol = self.__get_reg_val_symbol(symbol_node)
    else:
      symbol_addr_type = exp_tree_nodes[1]['symbol']
      symbol = str()
      if exp_tree_nodes[3]['type'] == 4:
        symbol_operation = exp_tree_nodes[3]['symbol']
        symbol_list = map(self.__get_reg_val_symbol, exp_tree_nodes[4:])
        symbol = '{}[{}]'.format(symbol_addr_type, ' {} '.format(symbol_operation).join(symbol_list))
      else:
        symbol = '{}[{}]'.format(symbol_addr_type, self.__get_reg_val_symbol(exp_tree_nodes[3]))
      self.type = 'memory'
      self.symbol = symbol
  
  def __get_reg_val_symbol(self, node):
      if node['type'] == 2:
        return hex(node['immediate'])
      else:
        return node['symbol']

  def __str__(self):
    return 'Operand: ' + {
      'address': self.address,
      'position': self.position,
      'expression_tree_id': self.expression_tree_id,
      'type': self.type,
      'data_type': self.data_type,
      'symbol': self.symbol,
    }.__str__()
