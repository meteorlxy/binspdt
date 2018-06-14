import json
from django.http import HttpResponse
from django.http import JsonResponse

def method_allow(methods_list):
  def decorator(view_func):
    def wrapped_view(request, *args, **kwargs):
      if request.method in methods_list:
        return view_func(request, *args, **kwargs)
      else:
        return HttpResponse(status=405)
    return wrapped_view
  return decorator

def api_view(request_json=True, response_json=True):
  def decorator(view_func):
    def wrapped_view(request, *args, **kwargs):
      if request_json and (request.method == 'POST'):
        request.json = json.loads(request.body.decode('utf-8'))
      response = view_func(request, *args, **kwargs)
      if response_json:
        if not isinstance(response, dict):
          response = dict()
        if 'err' not in response:
          response['err'] = 0
        if 'msg' not in response:
          response['msg'] = 'success'
        return JsonResponse(response)
      return response
    return wrapped_view
  return decorator
