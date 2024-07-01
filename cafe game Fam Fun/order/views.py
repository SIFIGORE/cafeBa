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

class getPrices(APIView):
    orders = orders
    queryset = orders.objects.all()
    Serializer_class = createOrderSerializer

    def post(self, request):
        data = json.loads(request.body)
        name = data.get('name')
        start_date = data.get('start_date')
        end_date = data.get('start_date')

        # تبدیل تاریخ‌ها به شیء datetime
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

        # فیلتر کردن داده‌ها بر اساس نام و بازه زمانی
        oorderss = self.orders.objects.filter(name=name, created__gte=start_date, created__lte=end_date)
        sumprice = 0
        response_data = []
        dateflag = None

        for order in oorderss:
            if dateflag is None or order.created == dateflag:
                sumprice += order.price
            else:
                response_data.append({
                    'name': order.name,
                    'date': dateflag,
                    'price': sumprice
                })
                sumprice = order.price

            dateflag = order.created

        # اضافه کردن آخرین روز
        if dateflag is not None:
            response_data.append({
                'name': name,
                'date': dateflag,
                'price': sumprice
            })

        return JsonResponse(response_data, status=status.HTTP_200_OK)
    