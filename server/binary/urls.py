from django.urls import path

from .views import modules
from .views import analysis_api

urlpatterns = [
  # Modules index
  path('modules', modules.index, name='modules.index'),
  # Module import
  path('modules/v/<ida_version>', modules.upload, name='modules.upload'),
  # Module detail and delete
  path('modules/<int:module_id>', modules.detail, name='modules.detail'),
  # Module load
  path('modules/<int:module_id>/load', modules.detail, name='modules.load'),
  # API Analysis
  path('analysis/api', analysis_api.index, name='analysis.api.index'),
]
