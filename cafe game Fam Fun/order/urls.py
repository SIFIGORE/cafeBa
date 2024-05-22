
from django.urls import include, path
from . import (views)
from rest_framework import routers
from .views import  ordersListApiView , ordersViewSet

router = routers.DefaultRouter()
router.register(r'order', ordersViewSet)


urlpatterns = [

    path('orders/all/', ordersListApiView.as_view() ,name='get_all_orders'),
    path('orders/addnew/', ordersViewSet.as_view('post'),name='post'),
    path('orders/' , include(router.urls))
]
