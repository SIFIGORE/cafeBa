
from django.urls import include, path
from . import (views)
# from rest_framework import routers
# from .views import  ordersViewSet

# router = routers.DefaultRouter()
# router.register(r'order', ordersViewSet)


urlpatterns = [

    # path('orders/all/', views.ordersListApiView.as_view() ,name='get_all_orders'),
    path('orders/addnew/', views.ordersViewSet.as_view('post')),
]
