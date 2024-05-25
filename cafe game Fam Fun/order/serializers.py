from asyncio.windows_events import NULL
from rest_framework import serializers
from order.models import orders
#from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField , JalaliDateTimeField
#from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields = ['name','price','created','get_jalali_date']

class getOrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = orders
        fields = ['name','price','created','get_jalali_date']

class createOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields = ['name','price']
        
 