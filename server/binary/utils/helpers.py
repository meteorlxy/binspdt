import json
from django.core.serializers import serialize

def model_serializable(model):
  data = serialize('json', [model,])
  data = json.loads(data)
  return data[0]['fields']