"""
utils - IDA Pro
"""
import os
from . import system

def get_ida_exe(ida_path, version, x64=False):
  """
  Get the IDA Pro Executable
  """
  # IDA Pro 6.x: idaq / idaq64
  # IDA Pro 7.x: ida / ida64
  exe_name = 'ida' if version.startswith('7') else 'idaq'

  if x64:
    exe_name = exe_name + '64'

  if system.is_windows():
    exe_name = exe_name + '.exe'

  return os.path.join(ida_path, exe_name)
