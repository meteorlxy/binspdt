"""
utils - system
"""
import platform

def is_windows():
  """
  Is running on Windows
  """
  return 'Windows' in platform.system()

def is_linux():
  """
  Is running on Linux
  """
  return 'Linux' in platform.system()
