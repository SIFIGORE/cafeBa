from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import foodSerializer
from .serializers import categorySerializer
from rest_framework import viewsets
from .models import category
from .models import food

class foodViewSet(viewsets.ModelViewSet):
   
   
   queryset = food.objects.all()
   serializer_class = foodSerializer

class foodListApiView(APIView):
    # add permission to check if user is authenticated
     

    # 1. List all
    def get(self, request, *args, **kwargs):
        
        foods = food.objects.all()
        serializer = foodSerializer(foods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class categoryViewSet(viewsets.ModelViewSet):
   
    
   
   queryset = category.objects.all()
   serializer_class = categorySerializer

class categoryListApiView(APIView):
    # add permission to check if user is authenticated
     

    # 1. List all
    def get(self, request, *args, **kwargs):
        
        categorys = category.objects.all()
        serializer = categorySerializer(categorys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)