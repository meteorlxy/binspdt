class BinaryRouter:
  """
  A router to control all database operations on models in the
  binary application.
  """
  def db_for_read(self, model, **hints):
    """
    Attempts to read binary models go to binary_db.
    """
    if model._meta.app_label == 'binary':
      return 'binary_db'
    return None

  def db_for_write(self, model, **hints):
    """
    Attempts to write binary models go to binary_db.
    """
    if model._meta.app_label == 'binary':
      return 'binary_db'
    return None

  def allow_relation(self, obj1, obj2, **hints):
    """
    Allow relations if a model in the binary app is involved.
    """
    if obj1._meta.app_label == 'binary' or \
      obj2._meta.app_label == 'binary':
      return True
    return None

  def allow_migrate(self, db, app_label, model_name=None, **hints):
    """
    Make sure the binary app only appears in the 'binary_db'
    database.
    """
    if app_label == 'binary':
      return db == 'binary_db'
    return None