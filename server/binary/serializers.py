from rest_framework import serializers
from .models import Module, ModuleAnalysis

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

class ModuleAnalysisSerializer(serializers.ModelSerializer):
  id = serializers.IntegerField(
    required=False,
  )

  description = serializers.CharField(
    required=True,
    min_length=1,
  )

  method = serializers.CharField(
    required=True,
  )

  params = serializers.JSONField(
    required=True,
    binary=False,
  )

  module_1_id = serializers.IntegerField(
    required=True,
  )
  module_2_id = serializers.IntegerField(
    required=True,
  )

  created_at = serializers.DateTimeField(
    required=False,
  )

  started_at = serializers.DateTimeField(
    required=False,
  )

  finished_at = serializers.DateTimeField(
    required=False,
  )

  failed_at = serializers.DateTimeField(
    required=False,
  )

  class Meta:
    model = ModuleAnalysis

    fields = (
      'id',
      'description',
      'method',
      'params',
      'module_1_id',
      'module_2_id',
      'created_at',
      'started_at',
      'finished_at',
      'failed_at',
    )

    read_only_fields = (
      'id',
      'created_at',
      'started_at',
      'finished_at',
      'failed_at',
    )

  def validate(self, data):
    """
    Check if the analysis fields valid
    """
    available_methods = (
      'api_set',
      'k_gram',
    )

    if data['method'] not in available_methods:
      raise serializers.ValidationError('Analysis method is unavailable.')
    
    if not Module.objects.filter(id=data['module_1_id']).exists() or not Module.objects.filter(id=data['module_2_id']).exists():
      raise serializers.ValidationError('Selected modules do not exist.')

    # TODO: Check params

    return data

class ModuleAnalysisDetailsSerializer(serializers.Serializer):
  
  id = serializers.IntegerField()
  description = serializers.CharField()
  method = serializers.CharField()
  params = serializers.JSONField()
  result = serializers.JSONField()
  module_1_id = serializers.IntegerField()
  module_2_id = serializers.IntegerField()
  created_at = serializers.DateTimeField()
  started_at = serializers.DateTimeField()
  finished_at = serializers.DateTimeField()
  failed_at = serializers.DateTimeField()
