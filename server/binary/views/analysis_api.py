from binary.utils import db
from binary.core.analysis.api import analyse_api
from binary.utils.decorators import method_allow, api_view

@method_allow(['POST'])
@api_view
def index(request):
  module_1_id = request.json['module_1']
  module_2_id = request.json['module_2']
  k = request.json['k']
  result = analyse_api(db=db, module_1_id=module_1_id, module_2_id=module_2_id, k=k)
  return {
    'data': result
  }
