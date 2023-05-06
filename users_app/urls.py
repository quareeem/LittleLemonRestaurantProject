from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register('group', views.GroupsView, basename='groups')
router.register('groups/all/users', views.UserViewset, basename='user_all')
router.register('groups/manager/users', views.UserManagerViewset, basename='user_manager')
router.register('groups/delivery-crew/users', views.UserDeliveryViewset, basename='user_delivery')

urlpatterns = [] + router.urls