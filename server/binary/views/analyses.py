from django.core.paginator import Paginator
from django.db.models import Q

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from binary import tasks
from binary.models import Module, ModuleObject, ModuleAnalysis
from binary.serializers import ModuleAnalysisSerializer, ModuleAnalysisDetailsSerializer
from binary.utils.helpers import normalize_api_result

class Analyses(ViewSet):
  """
  Handle analyses request
  """
  def index(self, request, format='json'):
    """
    Get analyses list
    """
    # get fields of analyses
    analysis_fields = tuple(field.name for field in ModuleAnalysis._meta.get_fields())
    qeuryset = ModuleAnalysis.objects.all()

    # get pagination params from query
    params = {
      'page': request.GET.get('_page', 1),
      'per_page': request.GET.get('_per_page', 25),
      'order_by': request.GET.get('_order_by', '-id'),
      'search': request.GET.get('_search', ''),
    }

    if params['search'] != '':
      qeuryset = qeuryset.filter(
        Q(description__contains = params['search'])
        | Q(method__contains = params['search'])
        # | Q(md5__contains = params['search'])
        # | Q(import_time__contains = params['search'])
      )

    if params['order_by'] not in analysis_fields:
      params['order_by'] = '-id'

    qeuryset = qeuryset.order_by(params['order_by'])

    paginator = Paginator(qeuryset, params['per_page'])
    page = paginator.get_page(params['page'])
    data = ModuleAnalysisSerializer(page.object_list, many=True).data

    return Response({
      'page': page.number,
      'page_count': paginator.num_pages,
      'data': data,
      'count': paginator.count,
    })

  def count(self, request, format='json'):
    """
    Get analyses count
    """
    return Response({
      'data': ModuleAnalysis.objects.count(),
    })

  def details(self, request, analysis_id, format='json'):
    """
    Get analysis details
    """
    qeuryset = ModuleAnalysis.objects.get(id=analysis_id)
    data = ModuleAnalysisDetailsSerializer(qeuryset).data

    if data['method'] == 'api_set':
      data['data'] = normalize_api_result(data['data'])
    return Response({
      'data': data,
    })
  
  def delete(self, request, analysis_id, format='json'):
    """
    Delete one analysis
    """
    try:
      ModuleAnalysis.objects.filter(id=analysis_id).delete()
      return Response({
        'msg': 'deleted analysis successfully',
        'data': {
          'analysis_id': analysis_id
        }
      }, status=status.HTTP_200_OK)
    except Exception:
      return Response({
        'msg': 'failed to delete analysis #' + analysis_id,
      }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def delete_many(self, request, format='json'):
    """
    Delete many analyses according to id
    """
    analyses = request.data['analyses']
    try:
      for analysis_id in analyses:
        ModuleAnalysis.objects.filter(id=analysis_id).delete()
      return Response({
        'msg': 'deleted analyses successfully',
        'data': {
          'analyses': analyses
        }
      }, status=status.HTTP_200_OK)
    except Exception:
      return Response({
        'msg': 'failed to delete analyses',
        'data': {
          'analyses': analyses
        }
      }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  
  def create(self, request, format='json'):
    """
    Create a analysis
    """
    
    params = request.data['params']
    description = request.data['description']
    method = request.data['method']
    module_1_id = request.data['modules'][0]
    module_2_id = request.data['modules'][1]

    serializer = ModuleAnalysisSerializer(data={
      'params': params,
      'description': description,
      'method': method,
      'module_1_id': module_1_id,
      'module_2_id': module_2_id,
    })
    
    if not serializer.is_valid():
      return Response({
        'msg': 'failed to create analysis',
        'errors': serializer.errors
      }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    new_analysis = serializer.save()

    if new_analysis:
      tasks.run_analysis.delay(new_analysis.id)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response({
        'msg': 'failed to create analysis',
      }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
