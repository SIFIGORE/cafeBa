from asyncio.windows_events import NULL
from rest_framework import serializers
from order.models import orders
#from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField , JalaliDateTimeField
#from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime



class ordersSerializer(serializers.ModelSerializer):

    class Meta:
        model = orders
        fields = ['name','price','created','get_jalali_date']


   # def jdate(self):

 #       self.fields['created'] = SplitJalaliDateTimeField(label=('created'),widget=AdminSplitJalaliDateTime)#label=('created'),widget=AdminSplitJalaliDateTime
    

        
 