import pickle
from os import path, makedirs, unlink
from django.conf import settings

STORAGE_DIR = settings.STORAGE_DIR

def resolve(*args):
  return path.normpath(path.join(STORAGE_DIR, *args))

def exists(target):
  target_path = resolve(target)
  return path.exists(target_path)

def write(target, content=None, force=False):
  """
  Write the [content] object to [target] file path in STORAGE_DIR
  """
  # resolve the target path and dir
  target_path = resolve(target)
  target_dir = path.dirname(target_path)

  # if the target path is dir, return False
  if path.isdir(target_path):
    return False

  # if the target file exists and force flag is False, return False
  if path.isfile(target_path) and not force:
    return False

  # if the target dir does not exist, create it
  if not path.isdir(target_dir):
    makedirs(target_dir)
  
  # dump the object to target file
  with open(target_path, 'wb') as f:
    pickle.dump(content, f)

  return True

def read(target):
  """
  Read the object from [target] file path in STORAGE_DIR
  """
  # resolve the target path
  target_path = resolve(target)

  # if the target file does not exist, return False
  if not path.isfile(target_path):
    return False

  # load the object from target file
  content = None
  with open(target_path, 'rb') as f:
    content = pickle.load(f)

  return content

def delete(target):
  """
  Delete the [target] file path in STORAGE_DIR
  """
  # resolve the target path
  target_path = resolve(target)

  # if the target file does not exist, return False
  if not path.isfile(target_path):
    return False
  
  # unlink the target file path
  unlink(target_path)

  return True
