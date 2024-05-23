from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import orders
from .serializers import ordersSerializer
from rest_framework import viewsets
from django.http import HttpResponse

class ordersViewSet(viewsets.ModelViewSet):
   
    
   
    queryset = orders.objects.all()
    serializer_class = ordersSerializer
    http_method_names = ['post']

    def post(self, request):
        return HttpResponse('POST request')

    def create(self, request, *args, **kwargs):
        
        queryset = orders.objects.all()
        serializer = ordersSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ordersListApiView(APIView):
    # add permission to check if user is authenticated
     

    # 1. List all
    def get(self, request, *args, **kwargs):
        
        queryset = orders.objects.all()
        serializer = ordersSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    