from ..asm import Module

def analyse_read_write_sequence(db, module_1_id, module_2_id):
  module_1 = Module(db=db, module_id=module_1_id).load().load_operands()
  module_2 = Module(db=db, module_id=module_2_id).load().load_operands()

  pass
