"""
utils - IDA Pro
"""
import os
from . import system

def get_ida_exe(ida_path, version, x64=False):
  """
  Get the IDA Pro Executable
  """
  if system.is_windows():
    return os.path.join(ida_path, 'idaq64.exe' if x64 else 'idaq.exe')
  else:
    return os.path.join(ida_path, 'idaq64' if x64 else 'idaq')
