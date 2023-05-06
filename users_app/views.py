from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404

from django.contrib.auth.models import Group, User

from .serializers import CurrentGroupSerializer, CurrentUserSerializer
# from .permissions import IsManagerOrReadOnly



class GroupsView(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = CurrentGroupSerializer


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer  



class UserManagerViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(groups__name='Manager')
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        user_name = request.data.get('username', None)
        user = get_object_or_404(self.queryset, username=user_name)
        group = Group.objects.get(name='Manager')
        user.groups.add(group)
        return Response({'msg': f'{user_name} added to a manager group'}, status=HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        user = get_object_or_404(self.queryset, pk=kwargs.get('pk', None))
        group = Group.objects.get(name='Manager')
        user.groups.remove(group)
        return Response({'msg': 'removed from manager group'}, status=HTTP_200_OK)
    


class UserDeliveryViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer   
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(groups__name='Delivery')
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('id', None)
        user = get_object_or_404(self.queryset, pk=user_id)
        group = Group.objects.get(name='Delivery')
        user.groups.add(group)
        return Response({'msg': 'added to a delivery crew'}, status=HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        user = get_object_or_404(self.queryset, pk=kwargs.get('pk', None))
        group = Group.objects.get(name='Delivery')
        user.groups.remove(group)
        return Response({'msg': 'removed from delivery crew'}, status=HTTP_200_OK)
    
    