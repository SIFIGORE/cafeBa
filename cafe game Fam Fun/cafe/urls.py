
from django.urls import include, path
from rest_framework import routers
from .views import foodListApiView , categoryListApiView , foodViewSet , categoryViewSet
from . import (views)

router = routers.DefaultRouter()
router.register(r'food', foodViewSet)
router.register(r'category', categoryViewSet)


urlpatterns = [

    path('food/all/', views.foodListApiView.as_view() ,name='get_all_food'),
    path('category/all/', views.categoryListApiView.as_view() ,name='get_all_category'),
    path('food/addnew/', include(router.urls)),
]
