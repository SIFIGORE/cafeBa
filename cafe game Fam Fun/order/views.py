import json
from venv import create
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics , status
from yaml import serialize
from .models import orders 
from .serializers import getOrdersSerializer , createOrderSerializer , orderSerializer
from rest_framework import viewsets
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import orders
from datetime import datetime
import jdatetime

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
    serializer_class = createOrderSerializer

    def post(self, request):
        data = json.loads(request.body)
        name = data.get('name')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        print(f"end_date is : {end_date}")
        # تبدیل تاریخ‌ها به شیء datetime
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        print("Initial data from DB:")
        for order in self.queryset.values():
            print(order)

        # فیلتر کردن داده‌ها بر اساس نام و بازه زمانی
        orders_list = self.queryset.filter(name=name, created__range=(start_date, end_date)).values()

        # چاپ تعداد داده‌های فیلتر شده برای اشکال‌زدایی
        print(f"Number of filtered orders: {len(orders_list)}")
        if len(orders_list) == 0:
            print(f"No orders found for name: {name} and date range: {start_date} to {end_date}")
        
        sum_price = 0
        response_data = []
        date_flag = None
        c = 0
        for order in orders_list:
            
            created_date = order['created']
            print(f"Processing order: {order}")  # چاپ داده‌های پردازش شده
            print(f"order created at: {order['created']}")
            print(f"order name is: {order['name']}")
            print(f"order price is: {order['price']}")
            print(f"sum_price is: {sum_price}") 
            print(f"date_flag is: {date_flag}") # چاپ داده‌های پردازش شده
            if start_date <= created_date <= end_date:
                if date_flag is None or created_date == date_flag:
                    sum_price += int(order['price'])
                    date_flag = created_date
                else:
                    print(f"we are in else and the order name is : {order['name']} and date_flag is : {date_flag} and sum_price is {sum_price}")
                    jalali_date = jdatetime.date.fromgregorian(day=date_flag.day, month=date_flag.month, year=date_flag.year)
                    response_data.append({
                        'name': order['name'],
                        'date': jalali_date,
                        'price': sum_price
                    })
                    sum_price = int(order['price'])
                    date_flag = created_date
                    c = c+1
            
        # اضافه کردن آخرین روز
        if date_flag is not None:
            jalali_date = jdatetime.date.fromgregorian(day=date_flag.day, month=date_flag.month, year=date_flag.year)
            response_data.append({
                'name': orders_list[c]['name'],
                'date': jalali_date,
                'price': sum_price
            })

        return Response(response_data, status=status.HTTP_200_OK)
    


class getPricesAll(APIView):
    queryset = orders.objects.all()
    serializer_class = createOrderSerializer

    def post(self, request):
        data = json.loads(request.body)
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        print(f"end_date is : {end_date}")
        # تبدیل تاریخ‌ها به شیء datetime
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        print("Initial data from DB:")
        for order in self.queryset.values():
            print(order)

        # فیلتر کردن داده‌ها بر اساس نام و بازه زمانی
        orders_list = self.queryset.filter(created__range=(start_date, end_date)).values()

        # چاپ تعداد داده‌های فیلتر شده برای اشکال‌زدایی
        print(f"Number of filtered orders: {len(orders_list)}")
        if len(orders_list) == 0:
            print(f"date range: {start_date} to {end_date}")
        
        sum_price = 0
        response_data = []
        date_flag = None
        c = 0
        for order in orders_list:
            
            created_date = order['created']
            print(f"Processing order: {order}")  # چاپ داده‌های پردازش شده
            print(f"order created at: {order['created']}")
            print(f"order price is: {order['price']}")
            print(f"sum_price is: {sum_price}") 
            print(f"date_flag is: {date_flag}") # چاپ داده‌های پردازش شده
            if start_date <= created_date <= end_date:
                if date_flag is None or created_date == date_flag:
                    sum_price += int(order['price'])
                    date_flag = created_date
                else:
                    print(f"date_flag is : {date_flag} and sum_price is {sum_price}")
                    jalali_date = jdatetime.date.fromgregorian(day=date_flag.day, month=date_flag.month, year=date_flag.year)
                    response_data.append({
                        'date': jalali_date,
                        'price': sum_price
                    })
                    sum_price = int(order['price'])
                    date_flag = created_date
                    c = c+1
            
        # اضافه کردن آخرین روز
        if date_flag is not None:
            jalali_date = jdatetime.date.fromgregorian(day=date_flag.day, month=date_flag.month, year=date_flag.year)
            response_data.append({
                'date': jalali_date,
                'price': sum_price
            })

        return Response(response_data, status=status.HTTP_200_OK)