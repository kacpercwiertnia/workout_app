from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Muscles
from .serializers import MusclesSerializer, RegisterSerializer, UserProfileSerializer, UpdateUserSerializer, UserGymSerializer, UserWorkoutSerializer, EquipmentsSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Users
from .models import Gyms
from .models import Workouts
from .models import Equipments
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
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

def UpdateUserView(request, pk):
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=404)
    
    data = JSONParser().parse(request)
    serializer = UserProfileSerializer(user, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


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
def getEquipments(request):
    equipments = Equipments.objects.all()
    serializer = EquipmentsSerializer(equipments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = User.objects.get(username = request.user)
    user_data = Users.objects.get(user = user)
    serializer = UserProfileSerializer(user_data)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserGyms(request):
    user = User.objects.get(username = request.user)
    user_data = Users.objects.get(user = user)
    user_gyms = Gyms.objects.filter(user_id=user_data.id)
    serializer = UserGymSerializer(user_gyms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserWorkouts(request):
    user = User.objects.get(username = request.user)
    user_data = Users.objects.get(user = user)
    user_workouts = Workouts.objects.filter(user_id=user_data.id)
    serializer = UserWorkoutSerializer(user_workouts, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def UpdateUserView(request,pk):
    user = Users.objects.get(id = pk)
    serializer = UpdateUserSerializer(instance = user, data = request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def CreateUserGyms(request):
    data = request.data
    user = User.objects.get(id = data['user_id'])
    user2 = Users.objects.get(user = user)
    user_gyms = Gyms.objects.create(gym_name = data['gym_name'], address = data['address'],
                                    user_id = user2, is_shared = False)

    serializer = UserGymSerializer(user_gyms, many=False)

    return Response(serializer.data)