
from django.urls import include, path
from rest_framework import routers
from .views import gameListApiView , gameViewSet
from . import (views)

router = routers.DefaultRouter()
router.register(r'game', gameViewSet)


urlpatterns = [

    path('game/all/', views.gameListApiView.as_view() ,name='get_all_game'),
    path('game/addnew/', include(router.urls)),
]
