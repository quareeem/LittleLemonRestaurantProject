from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import BaseUserManager, User, Group

from rest_framework.authtoken.models import Token
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

from .models import MenuItem, Category, Cart, Order



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']


class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=False, slug_field='title', queryset=Category.objects.all())

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category']


class CartSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=False, slug_field='username', many=False, queryset=User.objects.exclude(groups__name__in=['Manager', 'Delivery']))
    menuitem = serializers.SlugRelatedField(read_only=False, slug_field='title', many=False, queryset=MenuItem.objects.all())
    # menuitem = MenuItemSerializer(read_only=True)
    # user = CurrentUserSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'menuitem', 'user', 'quantity', 'unit_price', 'price']


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=False, slug_field='username', many=False, queryset=User.objects.exclude(groups__name__in=['Manager', 'Delivery']))
    delivery_crew = serializers.SlugRelatedField(read_only=False, allow_null=True, slug_field='username', many=False, queryset=User.objects.filter(groups__name='Delivery'))
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew', 'status', 'total', 'date']

        