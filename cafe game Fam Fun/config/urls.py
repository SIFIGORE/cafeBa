from django.conf.urls import url
from django.contrib import admin
from django.urls import path , include

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='cafe FAMFUN API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls') ),
    path('api/cafe/', include('cafe.urls')),
    path('api/gameroom/', include('game.urls')),
    url(r'^$', schema_view)
]

#router = DefaultRouter()
#router.register('user',DefaultViewSet,basename= 'user' )
#urlpatterns += router.urls  