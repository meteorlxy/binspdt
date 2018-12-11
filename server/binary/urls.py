from django.urls import path

from .views import modules
# from .views import analysis_api
# from .views import results

urlpatterns = [
  # Modules index
  path('modules', modules.Modules.as_view({ 'get': 'index', 'delete': 'delete_many' }), name='modules.index'),
  # Modules count
  path('modules/count', modules.Modules.as_view({ 'get': 'count' }), name='modules.count'),
  # Module details and delete
  path('modules/<int:module_id>', modules.Modules.as_view({ 'get': 'details', 'delete': 'delete' }), name='modules.details'),
  # Module import
  path('modules/v/<ida_version>', modules.Modules.as_view({ 'post': 'create' }), name='modules.upload'),
  # # API Analysis
  # path('analysis/api', analysis_api.index, name='analysis.api.index'),
  # # Results index
  # path('results', results.index, name='results.index'),
  # # Results detail
  # path('results/<int:result_id>', results.details, name='results.details'),
]
