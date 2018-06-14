from django.urls import path

from .views import modules
from .views import analysis_api
from .views import results

urlpatterns = [
  # Modules index
  path('modules', modules.index, name='modules.index'),
  # Module import
  path('modules/v/<ida_version>', modules.upload, name='modules.upload'),
  # Module details and delete
  path('modules/<int:module_id>', modules.details, name='modules.details'),
  # API Analysis
  path('analysis/api', analysis_api.index, name='analysis.api.index'),
  # Results index
  path('results', results.index, name='results.index'),
  # Results detail
  path('results/<int:result_id>', results.details, name='results.details'),
]
