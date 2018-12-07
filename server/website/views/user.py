from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class User(APIView):
  """
  Handle user request
  """
  def get(self, request, format='json'):
    """
    Get user info
    """
    return Response({
      'username': request.user.username,
      'email': request.user.email,
      'lastLogin': request.user.last_login,
    })
