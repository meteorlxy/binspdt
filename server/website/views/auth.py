from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from website.serializers.auth import RegisterSerializer, LoginSerializer

class Auth(ViewSet):
  """
  Handle user auth
  """
  permission_classes = (AllowAny,)

  def login(self, request, format='json'):
    """
    Login a user
    """
    serializer = LoginSerializer(data=request.data)
    if not serializer.is_valid():
      return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    user = authenticate(
      username=request.data['username'],
      password=request.data['password'],
    )
    if user is None:
      return Response({
        'msg': 'login failed'
      }, status=status.HTTP_401_UNAUTHORIZED)

    login(request, user)
    token, created = Token.objects.get_or_create(user=user)
    return Response({
      'username': user.username,
      'token': token.key,
    })

  def logout(self, request, format='json'):
    """
    Logout a user
    """
    if request.user.is_authenticated:
      Token.objects.filter(user=request.user).delete()
    logout(request)
    return Response(status=status.HTTP_200_OK)

  def register(self, request, format='json'):
    """
    Register new user
    """
    serializer = RegisterSerializer(data=request.data)
    if not serializer.is_valid():
      return Response({
        'msg': 'register failed',
        'errors': serializer.errors
      }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    user = serializer.save()
    if user:
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response({
        'msg': 'register failed',
      }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
