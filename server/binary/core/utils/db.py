"""
Use psycopg2 to connect to postgresql
See psycopg2[http://initd.org/psycopg/docs/usage.html]
"""
import os
import pickle
import psycopg2
from . import ida
from .binexport import Binexport

def zip_result(curs):
  colname_list = [desc[0] for desc in curs.description]
  result_list = list(dict((col, val) for col, val in zip(colname_list, result)) for result in curs)
  return result_list

class Database(object):
  """
  Database
  """
  def __init__(self, settings):
    self.settings = settings
    self.connection = psycopg2.connect(
      database=self.settings['POSTGRES']['NAME'],
      user=self.settings['POSTGRES']['USER'],
      password=self.settings['POSTGRES']['PASSWORD'],
      host=self.settings['POSTGRES']['HOST'],
      port=self.settings['POSTGRES']['PORT'],
    )

  def import_bin(self, file, x64, version='6.8'):
    """
    Import binary file into database
    """
    binex = Binexport(
      ida_exe=ida.get_ida_exe(self.settings['IDA'][version]['PATH'], version, x64),
      db_host=self.settings['POSTGRES']['HOST'],
      db_port=self.settings['POSTGRES']['PORT'],
      db_user=self.settings['POSTGRES']['USER'],
      db_password=self.settings['POSTGRES']['PASSWORD'],
      db_name=self.settings['POSTGRES']['NAME'],
      version=version,
    )
    return binex.import_bin(file)

  def import_idb(self, file, version='6.8'):
    """
    Import idb file into database
    """
    x64 = os.path.splitext(file)[1] == '.i64'
    binex = Binexport(
      ida_exe=ida.get_ida_exe(self.settings['IDA'][version]['PATH'], version, x64),
      db_host=self.settings['POSTGRES']['HOST'],
      db_port=self.settings['POSTGRES']['PORT'],
      db_user=self.settings['POSTGRES']['USER'],
      db_password=self.settings['POSTGRES']['PASSWORD'],
      db_name=self.settings['POSTGRES']['NAME'],
      version=version,
    )
    return binex.import_idb(file)

  def get_modules(self):
    """
    Get all modules from database
    """
    with self.connection as conn:
      with conn.cursor() as curs:
        curs.execute('SELECT * FROM modules')
        return zip_result(curs)

  def get_module(self, module_id):
    """
    Get a module from database
    """
    with self.connection as conn:
      with conn.cursor() as curs:
        curs.execute('SELECT * FROM modules WHERE id=%(module_id)s', {
          'module_id': module_id
        })
        result = zip_result(curs)
        if len(result) == 0:
          result = None
        else:
          result = result[0]
        return result

  def get_module_details(self, module_id):
    """
    Get details of a module from database
    """
    with self.connection as conn:
      with conn.cursor() as curs:
        curs.execute('SELECT \
          (SELECT COUNT(*) FROM ex_%(module_id)s_functions) AS functions_count, \
          (SELECT COUNT(*) FROM ex_%(module_id)s_basic_blocks) AS basic_blocks_count, \
          (SELECT COUNT(*) FROM ex_%(module_id)s_instructions) AS instructions_count', {
          'module_id': module_id,
        })
        result = zip_result(curs)
        return result[0]

  def get_callgraph(self, module_id):
    """
    Get callgraph of a module from database
    """
    with self.connection as conn:
      with conn.cursor() as curs:
        curs.execute('SELECT * FROM ex_%(module_id)s_callgraph', {
          'module_id': module_id,
        })
        return zip_result(curs)

  def get_control_flow_graph(self, module_id, function_address):
    """
    Get control_flow_graph of a function from database
    """
    with self.connection as conn:
      with conn.cursor() as curs:
        curs.execute('SELECT * FROM ex_%(module_id)s_control_flow_graphs \
          WHERE parent_function=%(function_address)s', {
          'module_id': module_id,
          'function_address': function_address,
        })
        return zip_result(curs)

  def get_module_functions(self, module_id):
    """
    Get all functions of a module from database
    """
    with self.connection as conn:
      with conn.cursor() as curs:
        curs.execute('SELECT * FROM ex_%(module_id)s_functions', {
          'module_id': module_id,
        })
        return zip_result(curs)
  
  def get_module_basic_blocks(self, module_id):
    """
    Get all functions & basic_blocks of a module from database
    """
    with self.connection as conn:
      with conn.cursor() as curs:
        curs.execute('SELECT func.*, \
          bb.id AS bb_id, bb.address AS bb_address, bb.parent_function AS bb_parent_function \
          FROM ex_%(module_id)s_functions AS func \
          INNER JOIN ex_%(module_id)s_basic_blocks AS bb ON bb.parent_function=func.address', {
          'module_id': module_id,
        })
        return zip_result(curs)

  def get_function_basic_blocks(self, module_id, function_address):
    """
    Get basic_blocks of a function from database
    """
    with self.connection as conn:
      with conn.cursor() as curs:
        curs.execute('SELECT * FROM ex_%(module_id)s_basic_blocks \
          WHERE parent_function=%(function_address)s', {
          'module_id': module_id,
          'function_address': function_address,
        })
        return zip_result(curs)

  def get_module_instructions(self, module_id):
    """
    Get all functions & basic_blocks & instructions of a module from database
    """
    with self.connection as conn:
      with conn.cursor() as curs:
        curs.execute('SELECT func.*, \
          bb.id AS bb_id, bb.address AS bb_address, bb.parent_function AS bb_parent_function, \
          inst.address AS inst_address, inst.mnemonic AS inst_mnemonic, inst.data AS inst_data \
          FROM ex_%(module_id)s_functions AS func \
          INNER JOIN ex_%(module_id)s_basic_blocks AS bb ON bb.parent_function=func.address \
          INNER JOIN ex_%(module_id)s_basic_block_instructions AS bb_inst ON bb.id=bb_inst.basic_block_id \
          INNER JOIN ex_%(module_id)s_instructions AS inst ON bb_inst.instruction=inst.address', {
          'module_id': module_id,
        })
        return zip_result(curs)

  def get_function_instructions(self, module_id, function_address):
    """
    Get all instructions of a function from database
    """
    with self.connection as conn:
      with conn.cursor() as curs:
        curs.execute('SELECT bb.*, \
          inst.address AS inst_address, inst.mnemonic AS inst_mnemonic, inst.data AS inst_data \
          FROM ex_%(module_id)s_basic_blocks AS bb \
          INNER JOIN ex_%(module_id)s_basic_block_instructions AS bb_inst ON bb.id=bb_inst.basic_block_id \
          INNER JOIN ex_%(module_id)s_instructions AS inst ON bb_inst.instruction=inst.address \
          WHERE bb.parent_function=%(function_address)s', {
          'module_id': module_id,
          'function_address': function_address,
        })
        return zip_result(curs)

  def get_basic_block_instructions(self, module_id, function_address=None, basic_block_id=None):
    """
    Get instructions of a function / basic_block from database
    """
    with self.connection as conn:
      with conn.cursor() as curs:
        if function_address != None:
          curs.execute('SELECT inst.address,mnemonic FROM ex_%(module_id)s_instructions AS inst \
            INNER JOIN ex_%(module_id)s_basic_block_instructions ON instruction=address \
            INNER JOIN ex_%(module_id)s_basic_blocks ON id=basic_block_id \
            WHERE parent_function=%(function_address)s',{
            'module_id': module_id,
            'function_address': function_address,
          })
        elif basic_block_id != None:
          curs.execute('SELECT address,mnemonic FROM ex_%(module_id)s_instructions \
            INNER JOIN ex_%(module_id)s_basic_block_instructions ON instruction=address \
            WHERE basic_block_id=%(basic_block_id)s', {
            'module_id': module_id,
            'basic_block_id': basic_block_id,
          })
        return zip_result(curs)
  
  def get_module_operands(self, module_id):
    """
    Get all functions & basic_blocks & instructions & operands of a module from database
    """
    with self.connection as conn:
      with conn.cursor() as curs:
        curs.execute('SELECT func.*, \
          bb.id AS bb_id, bb.address AS bb_address, bb.parent_function AS bb_parent_function, \
          inst.address AS inst_address, inst.mnemonic AS inst_mnemonic, inst.data AS inst_data, \
          op.position AS op_position, op.expression_tree_id AS op_expression_tree_id, op.address AS op_address \
          FROM ex_%(module_id)s_functions AS func \
          INNER JOIN ex_%(module_id)s_basic_blocks AS bb ON bb.parent_function=func.address \
          INNER JOIN ex_%(module_id)s_basic_block_instructions AS bb_inst ON bb.id=bb_inst.basic_block_id \
          INNER JOIN ex_%(module_id)s_instructions AS inst ON bb_inst.instruction=inst.address \
          INNER JOIN ex_%(module_id)s_operands AS op ON inst.address=op.address', {
          'module_id': module_id,
        })
        return zip_result(curs)
  
  def get_function_operands(self, module_id, function_address):
    """
    Get all basic_blocks & instructions & operands of a function from database
    """
    with self.connection as conn:
      with conn.cursor() as curs:
        curs.execute('SELECT bb.*, \
          inst.address AS inst_address, inst.mnemonic AS inst_mnemonic, inst.data AS inst_data, \
          op.position AS op_position, op.expression_tree_id AS op_expression_tree_id, op.address AS op_address \
          FROM ex_%(module_id)s_basic_blocks AS bb \
          INNER JOIN ex_%(module_id)s_basic_block_instructions AS bb_inst ON bb.id=bb_inst.basic_block_id \
          INNER JOIN ex_%(module_id)s_instructions AS inst ON bb_inst.instruction=inst.address \
          INNER JOIN ex_%(module_id)s_operands AS op ON inst.address=op.address \
          WHERE bb.parent_function=%(function_address)s', {
          'module_id': module_id,
          'function_address': function_address,
        })
        return zip_result(curs)
  
  def get_basic_block_operands(self, module_id, basic_block_id):
    """
    Get all instructions & operands of a basic_block from database
    """
    with self.connection as conn:
      with conn.cursor() as curs:
        curs.execute('SELECT inst.*, \
          op.position AS op_position, op.expression_tree_id AS op_expression_tree_id, op.address AS op_address \
          FROM ex_%(module_id)s_basic_block_instructions AS bb_inst \
          INNER JOIN ex_%(module_id)s_instructions AS inst ON bb_inst.instruction=inst.address \
          INNER JOIN ex_%(module_id)s_operands AS op ON inst.address=op.address \
          WHERE bb_inst.basic_block_id=%(basic_block_id)s', {
          'module_id': module_id,
          'basic_block_id': basic_block_id,
        })
        return zip_result(curs)

  def get_instruction_operands(self, module_id, instruction_address):
    """
    Get control_flow_graph of a function from database
    """
    with self.connection as conn:
      with conn.cursor() as curs:
        curs.execute('SELECT * FROM ex_%(module_id)s_operands \
          WHERE address=%(instruction_address)s', {
            'module_id': module_id,
            'instruction_address': instruction_address,
          })
        return zip_result(curs)
  
  def get_module_expression_trees(self, module_id):
    """
    Get all expression trees of a module from database
    """
    with self.connection as conn:
      with conn.cursor() as curs:
        curs.execute('SELECT exp_t_n.expression_tree_id AS tree_id, \
          exp_n.id,exp_n.type,exp_n.symbol,exp_n.immediate,exp_n.position,exp_n.parent_id \
          FROM ex_%(module_id)s_expression_tree_nodes AS exp_t_n \
          INNER JOIN ex_%(module_id)s_expression_nodes AS exp_n ON exp_t_n.expression_node_id=exp_n.id', {
          'module_id': module_id,
        })
        return zip_result(curs)

  def delete_module(self, module_id):
    """
    Delete a module according to the module id
    """
    with self.connection as conn:
      with conn.cursor() as curs:
        curs.execute("SELECT 'DROP TABLE IF EXISTS ' || tablename || ' CASCADE' FROM pg_tables \
          WHERE tablename like 'ex_%(module_id)s_%%';", {
          'module_id': module_id,
        })
        with conn.cursor() as curs2:
          for sql in curs:
            curs2.execute(sql[0])
          curs2.execute('DELETE FROM modules WHERE id=%(module_id)s', {
            'module_id': module_id,
          })
          curs2.execute('DELETE FROM module_objects WHERE id=%(module_id)s', {
            'module_id': module_id,
          })
  
  def save_module(self, module_id, obj, force=False):
    """
    Save the module pickled object to database
    """
    with self.connection as conn:
      with conn.cursor() as curs:
        if force:
          curs.execute('INSERT INTO module_objects(id, data) \
            VALUES(%(module_id)s, %(obj)s) \
            ON conflict(id) \
            DO UPDATE SET data=%(obj)s', {
            'module_id': module_id,
            'obj': pickle.dumps(obj),
          })
        else:
          curs.execute('INSERT INTO module_objects(id, data) \
            VALUES(%(module_id)s, %(obj)s) \
            ON conflict(id) \
            DO nothing', {
            'module_id': module_id,
            'obj': pickle.dumps(obj),
          })
  
  def load_module(self, module_id):
    """
    Load the module pickled object from database
    """
    with self.connection as conn:
      with conn.cursor() as curs:
        curs.execute('SELECT data FROM module_objects \
          WHERE id=%(module_id)s', {
          'module_id': module_id,
        })
        result = curs.fetchone()
        if result != None:
          result = pickle.loads(result[0])
        return result

  def __del__(self):
    self.connection.close()
