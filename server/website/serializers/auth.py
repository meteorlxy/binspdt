from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
  username = serializers.CharField(
    required=True,
    min_length=3,
    max_length=30,
    validators=[UniqueValidator(queryset=User.objects.all())],
  )

  email = serializers.EmailField(
    required=True,
    max_length=128,
  )

  password = serializers.CharField(
    required=True,
    min_length=8,
    max_length=30,
    write_only=True
  )

  first_name = serializers.CharField(
    required=False,
    max_length=30,
  )

  last_name = serializers.CharField(
    required=False,
    max_length=30,
  )

  class Meta:
    model = User
    fields = (
      'id',
      'username',
      'email',
      'first_name',
      'last_name',
      'password',
      'is_active',
      'is_staff',
      'last_login',
      'date_joined',
    )
    read_only_fields = (
      'id',
      'is_active',
      'is_staff',
      'last_login',
      'date_joined',
    )

  def create(self, validated_data):
    user = User.objects.create_user(
      username=validated_data['username'],
      email=validated_data['email'],
      password=validated_data['password'],
    )

    if 'first_name' in validated_data:
      user.first_name = validated_data['first_name']

    if 'last_name' in validated_data:
      user.last_name = validated_data['last_name']

    user.save()
    return user

class LoginSerializer(serializers.Serializer):
  username = serializers.CharField(
    required=True,
    min_length=3,
    max_length=30,
  )

  password = serializers.CharField(
    required=True,
    min_length=8,
    max_length=30,
  )
