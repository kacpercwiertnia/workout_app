from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Muscles
from .serializers import MusclesSerializer, RegisterSerializer, UserProfileSerializer, UpdateUserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Users
from rest_framework.permissions import AllowAny,IsAuthenticated
# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    ori_user_set = User.objects.all()
    my_user_set = Users.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UpdateUserView(generics.CreateAPIView):
    user_set = Users.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = ['/api/token', '/api/token/refresh','/api/muscles', '/api/register']
    return Response(routes)

@api_view(['GET'])
def getMuscles(request):
    muscles = Muscles.objects.all()
    serializer = MusclesSerializer(muscles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = User.objects.get(username = request.user)
    user_data = Users.objects.get(user = user)
    serializer = UserProfileSerializer(user_data)
    return Response(serializer.data)
