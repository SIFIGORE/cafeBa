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
    order = orders
    queryset = orders.objects.all()
    Serializer_class = createOrderSerializer

    def post(self, request):
        data = json.loads(request.body)
        naame = data.get('name')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        # تبدیل تاریخ‌ها به شیء datetime
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

        # فیلتر کردن داده‌ها بر اساس نام و بازه زمانی
        order_list = self.order.objects.filter(name = naame,created__range=(start_date, end_date)).values()
        sumprice = 0
        response_data = []
        dateflag = None

        for self.order.objects in order_list:
            created_date = self.order['created'].date()
            if start_date <= created_date <= end_date : 
                if dateflag is None or self.order.created == dateflag:
                    sumprice = self.order.price + sumprice
                    dateflag = self.order.created
                else:
                    response_data.append({
                        'name': self.order.name ,
                        'date': dateflag,
                        'price': sumprice
                    })
                    sumprice = self.order.price
                    dateflag = self.order.created
            # اضافه کردن آخرین روز
            # if dateflag is not None:
            #     response_data.append({
            #         'name': self.order.name,
            #         'date': dateflag,
            #         'price': sumprice
            #     }
            return JsonResponse(response_data, status=status.HTTP_200_OK , safe=False)
        if response_data is None :
            return Response(status=status.HTTP_400_BAD_REQUEST)