from django.urls import path

from .views.modules import Modules
from .views.analyses import Analyses
# from .views import analysis_api
# from .views import results

urlpatterns = [
  # Modules index and delete
  path('modules', Modules.as_view({ 'get': 'index', 'delete': 'delete_many' }), name='modules.index'),
  # Modules count
  path('modules/count', Modules.as_view({ 'get': 'count' }), name='modules.count'),
  # Module details and delete
  path('modules/<int:module_id>', Modules.as_view({ 'get': 'details', 'delete': 'delete' }), name='modules.details'),
  # Module import
  path('modules/import/<file_type>/<ida_version>', Modules.as_view({ 'post': 'create' }), name='modules.upload'),

  # Module functions
  path(
    'modules/<int:module_id>/functions',
    Modules.as_view({ 'get': 'module_functions' }),
    name='modules.functions',
  ),
  # Module function basic_blocks
  path(
    'modules/<int:module_id>/functions/<int:function_address>/basic_blocks',
    Modules.as_view({ 'get': 'function_basic_blocks' }),
    name='modules.functions.basic_blocks',
  ),
  # Module function basic_block instructions
  path(
    'modules/<int:module_id>/functions/<int:function_address>/basic_blocks/<int:basic_block_id>/instructions',
    Modules.as_view({ 'get': 'basic_block_instructions' }),
    name='modules.functions.basic_blocks.instructions',
  ),

  # Analyses index, create delete
  path('analyses', Analyses.as_view({ 'get': 'index', 'post': 'create', 'delete': 'delete_many' }), name='analyses.index'),
  # Analyses count
  path('analyses/count', Analyses.as_view({ 'get': 'count' }), name='analyses.count'),
  # Analysis details and delete
  path('analyses/<int:analysis_id>', Analyses.as_view({ 'get': 'details', 'delete': 'delete' }), name='analyses.details'),
]
