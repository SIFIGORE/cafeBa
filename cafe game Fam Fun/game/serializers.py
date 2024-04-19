from rest_framework import serializers
from game.models import game


class gameSerializer(serializers.ModelSerializer):

    class Meta:
        model = game
        fields = ['name','price']
    

        
 