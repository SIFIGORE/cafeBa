import json
from venv import create
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics , status
from .models import orders 
from .serializers import getOrdersSerializer , createOrderSerializer , orderSerializer
from rest_framework import viewsets
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import orders
from datetime import datetime

class ordersViewSet(viewsets.ModelViewSet):
   
    
   
   queryset = orders.objects.all()
   serializer_class = orderSerializer

class createOrdersViewSet(APIView):
    queryset = orders.objects.all()
    Serializer_class = createOrderSerializer

    def post(self, request):
        Serializer = createOrderSerializer(data=request.data, many=True)
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



class getPrices(APIView):
    queryset = orders.objects.all()
    Serializer_class = createOrderSerializer

    def post(self , request):
        data = json.loads(request.body)
        name = data.get('name')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        # تبدیل تاریخ‌ها به شیء datetime
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

        # فیلتر کردن داده‌ها بر اساس نام و بازه زمانی
        oorderss = self.orders.objects.filter( self.orders.name == name and self.orders.created >= start_date and self.orders.created <= end_date)
        sumprice = 0
        response_data = []
        for orders in oorderss:
            dateflag = self.orders.created
            if self.orders.created == dateflag :
                sumprice = self.orders.price + sumprice

            else:   
                response_data.append({
                'name': self.orders.name,
                'date': dateflag,
                'price': sumprice
                })
                sumprice = 0
                dateflag = self.orders.created
                sumprice = self.orders.price


        return JsonResponse(response_data, status=status.HTTP_200_OK)
    