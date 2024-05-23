from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import game
from .serializers import gameSerializer
from rest_framework import viewsets

class gameViewSet(viewsets.ModelViewSet):
   
    
   
   queryset = game.objects.all()
   serializer_class = gameSerializer

class gameListApiView(APIView):
    # add permission to check if user is authenticated
     

    # 1. List all
    def get(self, request, *args, **kwargs):
        
        games = game.objects.all()
        serializer = gameSerializer(games, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)