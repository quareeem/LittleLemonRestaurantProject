from django.contrib.auth.models import BaseUserManager, User, Group
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer


class CustomUserCreateSerializer(UserCreateSerializer):
    '''
    User registration (Djoser)
    '''
    class Meta(UserCreateSerializer.Meta):
        fields = ('email', 'username', 'password')


class CurrentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')

class CurrentUserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(read_only=False, slug_field='name', many=True, queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ('id', 'is_superuser','is_staff', "username", "first_name", "last_name", 'email', 'groups', 'user_permissions')

