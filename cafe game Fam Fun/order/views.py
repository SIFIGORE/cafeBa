from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics , status
from .models import orders 
from .serializers import getOrdersSerializer , createOrderSerializer , orderSerializer
from rest_framework import viewsets
from django.http import HttpResponse

class ordersViewSet(viewsets.ModelViewSet):
   
    
   
   queryset = orders.objects.all()
   serializer_class = orderSerializer

class createOrdersViewSet(APIView):
    queryset = orders.objects.all()
    Serializer_class = createOrderSerializer

    def post(self, request):
        Serializer = createOrderSerializer(data=request.data)
        if Serializer.is_valid(raise_exception = True):
            Serializer.save()
            return Response(Serializer.data, status=status.HTTP_201_CREATED)
        return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getOrdersViewSet(APIView):
    # add permission to check if user is authenticated
     

    # 1. List all
    def get(self, request, *args, **kwargs):
        
        queryset = orders.objects.all()
        serializer = getOrdersSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    