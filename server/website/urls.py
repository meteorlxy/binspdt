from django.urls import path

from .views import auth, user

urlpatterns = [
  path('auth/login', auth.Auth.as_view({ 'post': 'login' }), name='auth.login'),
  path('auth/logout', auth.Auth.as_view({ 'post': 'logout' }), name='auth.logout'),
  path('auth/register', auth.Auth.as_view({ 'post': 'register' }), name='auth.register'),
  path('user', user.User.as_view(), name='user'),
]
