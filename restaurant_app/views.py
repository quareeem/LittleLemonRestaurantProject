from datetime import date
from rest_framework.response import Response
from rest_framework.status import HTTP_207_MULTI_STATUS, HTTP_403_FORBIDDEN, HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_405_METHOD_NOT_ALLOWED
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404
from django.forms.models import model_to_dict
from django.db.models import Sum
from django.db.models.functions import Round


from django.contrib.auth.models import Group, User

from .models import MenuItem, Category, Cart, Order
from .serializers import MenuItemSerializer, CategorySerializer, CartSerializer, OrderSerializer
from .permissions import IsManagerOrReadOnly, IsStaffOrReadOnly
from users_app.serializers import CurrentUserSerializer


class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]


class MenuItemViewset(ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsStaffOrReadOnly]
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']


class CartViewset(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(user=request.user)
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        obj = get_object_or_404(queryset=self.queryset, menuitem=self.get_object().menuitem)
        if obj.user != request.user:
            return Response({f'Error': 'Permission Denied'}, status=HTTP_403_FORBIDDEN)
        self.queryset = self.queryset.filter(user=request.user)
        return super().retrieve(request, *args, **kwargs)
        

    def create(self, request, *args, **kwargs):
        title = request.data.get('title', None)
        item = get_object_or_404(MenuItem.objects.all(), title=title)

        if self.queryset.filter(user=request.user, menuitem=item.id).exists():
            instance = self.queryset.get(user=request.user, menuitem=item.id)
            data = self.get_serializer(instance=instance).data
            data['quantity'] += 1
            data['price'] = float(data['unit_price']) * data['quantity']
            serializer = self.get_serializer(instance, data=data)
        else:
            instance = MenuItem.objects.get(title=title)
            data = MenuItemSerializer(instance=instance).data
            data['user'] = request.user
            data['menuitem'] = item.title
            data['unit_price'] = item.price
            data['quantity'] = 1
            serializer = self.get_serializer(data=data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)
    

    def destroy(self, request, *args, **kwargs):
        self.perform_destroy(self.queryset.filter(user=request.user))
        return Response({'msg': 'Cart has been deleted'}, status=HTTP_204_NO_CONTENT)




class OrderViewset(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def identify(self, request):
        group = list(User.objects.get(username=request.user).groups.all().values())
        if len(group) == 0:
            return 'Customer'
        return group[0]['name']
    
    def list(self, request, *args, **kwargs):
        identity = self.identify(request)
        if identity == 'Customer':
            self.queryset = self.queryset.filter(user=request.user)
            print('thi si user')
        elif identity == 'Manager':
            pass
        elif identity == 'Delivery':
            self.queryset = self.queryset.filter(delivery_crew__isnull=False)
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        identity = self.identify(request)
        if identity == 'Customer':
            self.queryset = self.queryset.filter(user=request.user)
            total = Cart.objects.filter(user=request.user).aggregate(total_sum=Round(Sum('price'), 2))
            data = {
                'user': request.user,
                'delivery_crew': None,
                'date': date.today(),
                'total': float(total['total_sum'])
                }
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            # clear the cart
            cart_queryset = Cart.objects.filter(user=request.user)
            cart_queryset.delete()

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)
        return Response({'Error': 'Method Not Allowed'}, status=HTTP_405_METHOD_NOT_ALLOWED)
    
    def retrieve(self, request, *args, **kwargs):
        identity = self.identify(request)
        if identity == 'Customer':
            self.queryset = Cart.objects.filter(user=request.user)
            self.serializer_class = CartSerializer
            return super().list(request, *args, **kwargs)
        return Response({'Error': 'Forbidden'}, status=HTTP_405_METHOD_NOT_ALLOWED)
    
    def update(self, request, *args, **kwargs):
        identity = self.identify(request) 
        if identity == 'Manager':
            return super().update(request, *args, **kwargs)
        if identity == 'Delivery':
            if set(request.data.keys()) == {'status'}:
                return super().update(request, *args, **kwargs)
            return Response({'Error': 'Field change other than \'status\' is not allowed'}, status=HTTP_405_METHOD_NOT_ALLOWED)
        return Response({'Error': 'Forbidden'}, status=HTTP_405_METHOD_NOT_ALLOWED)
    

    def destroy(self, request, *args, **kwargs):
        if self.identify(request) == 'Manager':
            return super().destroy(request, *args, **kwargs)
        return Response({'Error': 'Forbidden'}, status=HTTP_405_METHOD_NOT_ALLOWED)
       
