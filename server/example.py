import django
from binspdt import settings
django.setup()

from binary.core.asm import Module
from binary.utils import db


module = Module(db, 1).load().load_expression_trees()

exp_tree = module.expression_trees[593]

print(exp_tree)


###### Instruction sequence

# module = Module(db, 1).load().load_operands()

# function = module.functions[list(module.functions.keys())[0]]

# basic_block_1 = function.basic_blocks[list(function.basic_blocks.keys())[0]]
# basic_block_2 = function.basic_blocks[list(function.basic_blocks.keys())[2]]

# mnemonic_seq_1 = []
# mnemonic_seq_2 = []

# for inst in basic_block_1.instructions.values():
#   mnemonic_seq_1.append(inst.mnemonic)
# for inst in basic_block_2.instructions.values():
#   mnemonic_seq_2.append(inst.mnemonic)

# print(mnemonic_seq_1)
# print(mnemonic_seq_2)





'''
Init a module
'''
# module = Module(db=db, module_id=1)
# print(module)

'''
Module Level load
'''
# '''Load all functions of a module'''
# module.load_functions()
# functions = module.functions
# function = functions[list(functions.keys())[0]]
# print(function)

# '''Load all functions and basic_blocks of a module'''
# module.load_basic_blocks()
# functions = module.functions
# function = functions[list(functions.keys())[0]]
# print(function)

# basic_blocks = function.basic_blocks
# basic_block = basic_blocks[list(basic_blocks.keys())[0]]
# print(basic_block)

# '''Load all functions and basic_blocks and instructions of a module'''
# module.load_instructions()
# functions = module.functions
# function = functions[list(functions.keys())[0]]
# print(function)
# basic_blocks = function.basic_blocks
# basic_block = basic_blocks[list(basic_blocks.keys())[0]]
# print(basic_block)
# instructions = basic_block.instructions
# instruction = instructions[list(instructions.keys())[0]]
# print(instruction)

# '''Load all functions and basic_blocks and instructions and operands of a module'''
# module.load_operands()
# functions = module.functions
# function = functions[list(functions.keys())[0]]
# print(function)
# basic_blocks = function.basic_blocks
# basic_block = basic_blocks[list(basic_blocks.keys())[0]]
# print(basic_block)
# instructions = basic_block.instructions
# instruction = instructions[list(instructions.keys())[0]]
# print(instruction)
# operands = instruction.operands
# if len(operands) != 0:
#   operand = operands[list(operands.keys())[0]]
#   print(operand)

'''
Function Level load
'''
# module.load_functions()
# functions = module.functions
# function = functions[list(functions.keys())[0]]
# print(function)

# '''Load all basic_blocks of a function'''
# function = function.load_basic_blocks()
# basic_blocks = function.basic_blocks
# basic_block = basic_blocks[list(basic_blocks.keys())[0]]
# print(basic_block)

# '''Load all basic_blocks and instructions of a function'''
# function = function.load_instructions()
# basic_blocks = function.basic_blocks
# basic_block = basic_blocks[list(basic_blocks.keys())[0]]
# print(basic_block)
# instructions = basic_block.instructions
# instruction = instructions[list(instructions.keys())[0]]
# print(instruction)

# '''Load all basic_blocks and instructions and operands of a function'''
# function = function.load_operands()
# basic_blocks = function.basic_blocks
# basic_block = basic_blocks[list(basic_blocks.keys())[0]]
# print(basic_block)
# instructions = basic_block.instructions
# instruction = instructions[list(instructions.keys())[0]]
# print(instruction)
# operands = instruction.operands
# if len(operands) != 0:
#   operand = operands[list(operands.keys())[0]]
#   print(operand)


'''
Basic Block Level load
'''
# module.load_functions()
# functions = module.functions
# function = functions[list(functions.keys())[0]]
# function.load_basic_blocks()
# basic_blocks = function.basic_blocks
# basic_block = basic_blocks[list(basic_blocks.keys())[0]]
# print(basic_block)

# '''Load all instructions of a basic_block'''
# basic_block = basic_block.load_instructions()
# instructions = basic_block.instructions
# instruction = instructions[list(instructions.keys())[0]]
# print(instruction)

# '''Load all instructions and operands of a basic_block'''
# basic_block = basic_block.load_operands()
# instructions = basic_block.instructions
# instruction = instructions[list(instructions.keys())[0]]
# print(instruction)
# operands = instruction.operands
# if len(operands) != 0:
#   operand = operands[list(operands.keys())[0]]
#   print(operand)


'''
Instruction Level load
'''
# module.load_functions()
# functions = module.functions
# function = functions[list(functions.keys())[0]]
# function.load_basic_blocks()
# basic_blocks = function.basic_blocks
# basic_block = basic_blocks[list(basic_blocks.keys())[0]]
# basic_block = basic_block.load_instructions()
# instructions = basic_block.instructions
# instruction = instructions[list(instructions.keys())[0]]
# print(instruction)

# '''Load all operands of a instruction'''
# instruction = instruction.load_operands()
# operands = instruction.operands
# if len(operands) != 0:
#   operand = operands[list(operands.keys())[0]]
#   print(operand)


'''
Load the detail of module step by step
'''
# '''Load functions / callgraph of the module'''
# module = module.load_functions().load_callgraph()
# print(module)

# '''Get the first function of the module'''
# functions = module.functions
# function = functions[list(functions.keys())[0]]
# print(function)

# '''Load basic block / CFG of the function'''
# function = function.load_basic_blocks().load_control_flow_graph()
# print(function)

# '''Get the first basic block of the function'''
# basic_blocks = function.basic_blocks
# basic_block = basic_blocks[list(basic_blocks.keys())[0]]
# print(basic_block)

# '''Load instructions of the basic block'''
# basic_block = basic_block.load_instructions()
# print(basic_block)

# '''Get the first instruction of the basic block'''
# instructions = basic_block.instructions
# instruction = instructions[list(instructions.keys())[0]]
# print(instruction)

# '''Load operands of the instruction'''
# instruction = instruction.load_operands()
# print(instruction)

# '''Get the first operand (if has) of the instruction'''
# operands = instruction.operands
# if len(operands) != 0:
#   operand = operands[list(operands.keys())[0]]
#   print(operand)


'''
Save and Load module
'''
# '''Save the module object to database'''
# module.save()

# '''Load existed module from databse according to de module_id'''
# newModule = Module(db=db, module_id=1)
# print(newModule)
# newModule.load()
# print(newModule)


'''
Similarity Analysis
'''
'''API Similarity'''
# analyse_api(db=db, module_1_id=1, module_2_id=3)