from django.db import models

class Module(models.Model):
  id = models.IntegerField(primary_key=True)
  name = models.TextField()
  architecture = models.CharField(max_length=32)
  base_address = models.BigIntegerField()
  exporter = models.CharField(max_length=256)
  version = models.IntegerField()
  md5 = models.CharField(max_length=32)
  sha1 = models.CharField(max_length=40)
  comment = models.TextField()
  import_time = models.DateTimeField(auto_now=True)

  class Meta:
    app_label = 'binary'
    db_table = 'modules'

class ModuleObject(models.Model):
  id = models.OneToOneField(Module, on_delete=models.CASCADE, primary_key=True, db_column='id')
  data = models.BinaryField()

  class Meta:
    app_label = 'binary'
    db_table = 'module_objects'

class ModuleResultObject(models.Model):
  id = models.CharField(max_length=256, primary_key=True)
  data = models.BinaryField()

  class Meta:
    app_label = 'binary'
    db_table = 'module_result_objects'
