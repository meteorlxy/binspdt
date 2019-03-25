"""
Use binexport to import idb file to PostgreSQL database
See google/binexport[https://github.com/google/binexport]
"""
import subprocess
import os
import tempfile

class Binexport(object):
  """
  use binexport to import idb file into postgresql database
  """

  version_map = {
    '6.8': 8,
    '6.95': 9,
    '7.0': 10,
    '7.1': 10,
    '7.2': 10,
  }

  def __init__(
    self,
    ida_exe,
    db_host,
    db_port,
    db_user,
    db_password,
    db_name,
    db_schema='public',
    version='6.8',
  ):
    """
    init the Binexport instance
    """
    self.ida_exe = ida_exe
    self.db_host = db_host
    self.db_port = db_port
    self.db_user = db_user
    self.db_password = db_password
    self.db_name = db_name
    self.db_schema = db_schema
    self.version = self.version_map[version]
  
  def import_bin(self, bin_file):
    """
    import binary file into database
    """
    self.__run_import_script(file=bin_file, is_bin=True)

  def import_idb(self, idb_file):
    """
    import idb file into database
    """
    self.__run_import_script(file=idb_file, is_bin=False)
  
  def __run_import_script(self, file, is_bin):
    # write the temp idc file
    idc_tmp = tempfile.mkstemp()
    self.__write_idc_tmp(idc_tmp)

    ida_command = [self.ida_exe]

    if is_bin == True:
      ida_command.append('-c')
    
    ida_command.append('-A')

    if self.version < 10:
      ida_command.extend([
        '-OExporterHost:' + self.db_host,
        '-OExporterPort:' + self.db_port,
        '-OExporterUser:' + self.db_user,
        '-OExporterPassword:' + self.db_password,
        '-OExporterDatabase:' + self.db_name,
        '-OExporterSchema:' + self.db_schema,
      ])
    
    ida_command.extend([
      r'-S"' + idc_tmp[1] + r'"',
      file,
    ])

    try:
      # call ida_exe with the temp idc file
      subprocess.check_output(ida_command)
    finally:
      # remove the temp idc file after finish
      os.remove(idc_tmp[1])

  def __write_idc_tmp(self, idc_tmp):
    """
    write binexport idc script
    """
    with os.fdopen(idc_tmp[0], 'w') as idc:
      if self.version < 10:
        idc.write('''
          #include <idc.idc>
          static main()
          {
            SetShortPrm(INF_AF2, GetShortPrm(INF_AF2) | AF2_DODATA);
            Wait();
            RunPlugin("zynamics_binexport_%s", 1);
            Exit(0);
          }
        ''' % self.version)
      else:
        idc.write('''
          #include <idc.idc>
          static main() {
            set_inf_attr(INF_AF, get_inf_attr(INF_AF) | AF_DODATA);
            auto_wait();
            BinExportSql("%(host)s", %(port)s, "%(database)s", "%(schema)s", "%(user)s", "%(password)s");
            qexit(0);
          }
        ''' % {
          'host': self.db_host,
          'port': self.db_port,
          'user': self.db_user,
          'password': self.db_password,
          'database': self.db_name,
          'schema': self.db_schema,
        })
