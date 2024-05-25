from rest_framework import serializers
from cafe.models import food
from cafe.models import category


class foodSerializer(serializers.ModelSerializer):

    class Meta:
        model = food
        fields = ['id','name', 'category','price']
    
        
class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ['id','name'] 