from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register('category', views.CategoryViewset, basename='category')
router.register('menu-items', views.MenuItemViewset, basename='menuitem')
router.register('cart/menu-items', views.CartViewset, basename='cart')
router.register('orders', views.OrderViewset, basename='order')
# router.register('orders/<int:order_id>', views.OrderIDViewset, basename='order_id')



urlpatterns = [
    # path('category/{int:pk}', views.CategoriesView.as_view()),
    # path('menu-items/', views.MenuItemsView.as_view()),
    # path('manager/', views.manager_view),
    # path('groups/<str:userType>/users', views.UsersView.as_view())
] + router.urls