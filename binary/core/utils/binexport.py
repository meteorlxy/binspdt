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
    self.version = version

  def import_idb(self, idb_file):
    """
    import idb file into database
    """
    idc_tmp = tempfile.mkstemp()
    self.__write_idc_tmp(idc_tmp)
    subprocess.call([
      self.ida_exe,
      '-A',
      '-OExporterHost:' + self.db_host,
      '-OExporterPort:' + self.db_port,
      '-OExporterUser:' + self.db_user,
      '-OExporterPassword:' + self.db_password,
      '-OExporterDatabase:' + self.db_name,
      '-OExporterSchema:' + self.db_schema,
      r'-S"' + idc_tmp[1] + r'"',
      idb_file
    ])
    os.remove(idc_tmp[1])

  def __write_idc_tmp(self, idc_tmp):
    """
    write binexport idc script
    """
    with os.fdopen(idc_tmp[0], 'w') as idc:
      idc.write("""
        #include <idc.idc>
        static main()
        {
          Batch(0);
          Wait();
          RunPlugin("zynamics_binexport_%s", 1);
          Exit(0);
        }
      """ % self.version_map[self.version])
