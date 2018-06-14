from django.core.paginator import Paginator
from binary.utils.decorators import method_allow, api_view
from binary.utils.helpers import model_serializable
from binary.utils import storage

from binary.models import ModuleResult

@method_allow(['GET'])
@api_view()
def index(request):
  page = request.GET.get('page', 1)
  per_page = request.GET.get('perpage', 20)

  results_all = ModuleResult.objects.all().order_by('-id')

  results_pages = Paginator(results_all, per_page)

  results = results_pages.page(page).object_list.values()

  return {
    'data': {
      'data': list(results),
      'count': results_pages.count,
      'num_pages': results_pages.num_pages,
      'page': page,
      'per_page': per_page
    }
  }

@method_allow(['GET'])
@api_view()
def details(request, result_id):
  result = ModuleResult.objects.get(id=result_id)
  result_path = result.path

  result_obj = storage.read(result_path)

  return {
    'data': result_obj
  }
