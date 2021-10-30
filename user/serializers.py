from rest_framework import serializers
from . import models
from djoser.serializers import UserCreateSerializer, UserSerializer


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'email', 'username', 'password')
