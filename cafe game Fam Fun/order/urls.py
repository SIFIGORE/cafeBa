
from django.urls import include, path
from . import (views)
from rest_framework import routers
from .views import  getOrdersViewSet , createOrdersViewSet , ordersViewSet

router = routers.DefaultRouter()
router.register(r'order', ordersViewSet)


urlpatterns = [

    path('orders/all/', getOrdersViewSet.as_view() ,name='get_all_orders'),
    path('orders/addnew/', createOrdersViewSet.as_view(),name='post_all_orders'),
    #path('orders/' , include(router.urls))
]
