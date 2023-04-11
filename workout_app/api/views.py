from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Muscles
from .serializers import MusclesSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(request):

    return Response('Out API')

@api_view(['GET'])
def getMuscles(request):
    muscles = Muscles.objects.all()
    serializer = MusclesSerializer(muscles, many=True)
    return Response(serializer.data)