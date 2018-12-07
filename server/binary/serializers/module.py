from rest_framework import serializers
from binary.models import Module

class ModuleSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  name = serializers.CharField()
  architecture = serializers.CharField()
  base_address = serializers.IntegerField()
  exporter = serializers.CharField()
  version = serializers.IntegerField()
  md5 = serializers.CharField()
  sha1 = serializers.CharField()
  comment = serializers.CharField()
  import_time = serializers.DateTimeField()
