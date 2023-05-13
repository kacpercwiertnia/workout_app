from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Muscles
from .serializers import MusclesSerializer, RegisterSerializer, UserProfileSerializer, UpdateUserSerializer, UserGymSerializer, UserWorkoutSerializer, EquipmentsSerializer, GymEqupiment
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Users
from .models import Gyms
from .models import Shared_gyms
from .models import Workouts
from .models import Workout_details
from .models import Equipments
from .models import Gym_details
from .models import Exercises
from django.db.models import Q
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import random
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
def getAllUserGyms(request):
    user = User.objects.get(username = request.user)
    user_data = Users.objects.get(user = user)
    user_gyms = Gyms.objects.filter(user_id=user_data.id)
    user_gyms2 = Shared_gyms.objects.filter(user_id = user_data.id)
    for el in user_gyms2.values():
        gym = Gyms.objects.filter(id=el['gym_id_id'])
        user_gyms |= gym
    serializer = UserGymSerializer(user_gyms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserGym(request, pk):
    user = User.objects.get(username = request.user)
    user_data = Users.objects.get(user = user)
    user_gyms = Gyms.objects.filter(user_id=user_data.id)
    gym = user_gyms.get(id = pk)
    serializer = UserGymSerializer(gym, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getGymEqupiments(request, pk):
    user = User.objects.get(username = request.user)
    user_data = Users.objects.get(user = user)
    user_gyms = Gyms.objects.filter(user_id=user_data.id)
    gym = user_gyms.get(id = pk)
    equipments = Gym_details.objects.filter(gym_id = gym)
    serializer = GymEqupiment(equipments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserWorkouts(request):
    user = User.objects.get(username = request.user)
    user_data = Users.objects.get(user = user)
    user_workouts = Workouts.objects.filter(user_id=user_data.id)
    workouts = []
    for el in user_workouts.values():
        muscle = Muscles.objects.get(id= el['muscle_id_id']).muscle_name
        gym = Gyms.objects.get(id = el['gym_id_id']).gym_name
        workouts.append({'id':el['id'], 'muscle': muscle, 'gym': gym, 'date': el['date']})
    return Response(workouts)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserWorkout(request, pk):
    user = User.objects.get(username = request.user)
    user_data = Users.objects.get(user = user)
    user_workout = Workouts.objects.get(id = pk, user_id=user_data.id)
    serializer = UserWorkoutSerializer(user_workout)
    muscle = Muscles.objects.get(id= serializer.data['muscle_id']).muscle_name
    gym = Gyms.objects.get(id= serializer.data['gym_id']).gym_name
    date = serializer.data['date']
    data = [{'muscle': muscle, 'gym': gym, 'date':date}]
    details = Workout_details.objects.filter(workout_id = user_workout)
    for el in details.values():
        exercies = Exercises.objects.get(id = el['exercise_id_id'])
        equipment = Equipments.objects.get(equipment_name = exercies.equipment_id).equipment_name
        data.append({'exercise_name': exercies.exercise_name, 'equipment': equipment, 'description': el['description'], 'id': el['exercise_id_id']})
    return Response(data)

@api_view(['GET'])
def checkIfGymAdded(request, pk):
    user = User.objects.get(username = request.user)
    user2 = Users.objects.get(user = user)
    gym = Gyms.objects.get(id = pk)
    found = Shared_gyms.objects.filter(gym_id=gym, user_id = user2)

    if(found.count() != 0):
        return Response(True)
    return Response(False)

@api_view(['PUT', 'DELETE'])
def addOrDeleteSharedGymToUserGyms(request, pk):
    data = request.data
    user = User.objects.get(id = data['user_id'])
    user2 = Users.objects.get(user = user)
    gym = Gyms.objects.get(id = pk)
    found = Shared_gyms.objects.filter(gym_id=gym, user_id = user2)

    if(not data['action'] and found.count() != 0):
        found.delete()
        return Response("Gym removed from your list")
    elif(not data['action'] and found.count() == 0):
        return Response("Gym is not on your list")
    elif(data['action'] and found.count() != 0):
        return Response("Gym is already on your list")
    elif(data['action'] and found.count() == 0):
        Shared_gyms.objects.create(gym_id=gym, user_id=user2)
        return Response("Gym added to your list")

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def changeExercise(request, pk):
    exercise_id_data = request.data.get('exercise_id')
    current_exercises = [exercise_id_data]

    user = User.objects.get(username = request.user)
    user_data = Users.objects.get(user = user)
    user_workout = Workouts.objects.get(id = pk, user_id=user_data.id)
    details = Workout_details.objects.filter(workout_id = user_workout)
    to_delete = Workout_details.objects.filter(workout_id = user_workout, exercise_id_id = exercise_id_data)
    to_delete.delete()
    for el in details.values():
        current_exercises.append(el['exercise_id_id'])

    muscle = Muscles.objects.get(id = user_workout.muscle_id.id)
    gym = Gyms.objects.get(id = user_workout.gym_id.id)
    user_exp = user_data.experience
    gym_equpiment = Gym_details.objects.filter(gym_id = gym).values()
    potential_workout = []
    for el in gym_equpiment:
        equipment = Equipments.objects.get(id = el['equipment_id_id'])
        exercise = Exercises.objects.filter(equipment_id = equipment, muscle_id = muscle, difficulty = user_exp)
        if exercise.count() >= 1:
            for el2 in  exercise.values():
                exer = Exercises.objects.get(id = el2['id'])
                desc = el2['description']
                potential_workout.append({'exercise_id': exer, 'description': desc})
    if len(potential_workout) > 5:
        while True:
            candidate_number = random.randint(0, len(potential_workout)-1)
            candidate = potential_workout[candidate_number]
            if candidate['exercise_id'].id not in current_exercises:
                Workout_details.objects.create(workout_id = user_workout, exercise_id = candidate['exercise_id'], description = candidate['description'])
                break
        return Response("Exercise has been changed!")
    else:
        return Response("Can't cahnge the exercise!")

@api_view(['PUT'])
def UpdateUserView(request,pk):
    user = Users.objects.get(id = pk)
    serializer = UpdateUserSerializer(instance = user, data = request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['PUT', 'DELETE']) 
def UpdateUserGym(request,pk):
    gym = Gyms.objects.get(id = pk)
    
    for el in request.data:
        equipment = Equipments.objects.get(id = el['equipment_id'])
        if el['is_checked']:
            in_gym = Gym_details.objects.filter(gym_id = gym, equipment_id = equipment)
            if in_gym.count() == 0:
                Gym_details.objects.create(gym_id = gym, equipment_id = equipment, quantity = 1)
        else:
            in_gym = Gym_details.objects.filter(gym_id = gym, equipment_id = equipment)
            if in_gym.count() == 1:
                in_gym.delete()
    
    return Response("Gym was updated!")

@api_view(['POST'])
def CreateUserGyms(request):
    data = request.data
    user = User.objects.get(id = data['user_id'])
    user2 = Users.objects.get(user = user)
    user_gyms = Gyms.objects.create(gym_name = data['gym_name'], address = data['address'],
                                    user_id = user2, is_shared = False)

    serializer = UserGymSerializer(user_gyms, many=False)

    return Response(serializer.data)

@api_view(['PUT'])
def ShareGym(request, pk):
  data = request.data
  gym = Gyms.objects.get(id=pk)
  gym.is_shared = data['is_shared']
  gym.save()
  serializer = UserGymSerializer(gym, many=False)
  return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetSharedGyms(request):
    user = User.objects.get(username = request.user)
    user2 = Users.objects.get(user = user)
    shared_gyms = Gyms.objects.filter(~Q(user_id=user2, is_shared=True) )
    public_gyms = []
    for el in shared_gyms.values():
        public_gyms.append({'id': el['id'], 'name': el['gym_name'], 'addres': el['address']})
    return Response(public_gyms)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getPublicGymEqupiments(request, pk):
    gym = Gyms.objects.get(id = pk)
    equipments = Gym_details.objects.filter(gym_id = gym)
    serializer = GymEqupiment(equipments, many=True)
    public_gym_equipments = []
    for el in serializer.data:
        equipment = Equipments.objects.get(id = el['equipment_id']).equipment_name
        public_gym_equipments.append({'id': el['equipment_id'], 'eq_name': equipment})
    return Response(public_gym_equipments)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateUserWorkout(request):
    user = User.objects.get(username = request.user)
    user_data = Users.objects.get(user = user)
    user_exp = user_data.experience
    data = request.data
    muscle = Muscles.objects.get(id = data['muscle_id'])
    gym = Gyms.objects.get(id = data['gym_id'])
    gym_equpiment = Gym_details.objects.filter(gym_id = gym).values()
    potential_workout = []
    for el in gym_equpiment:
        equipment = Equipments.objects.get(id = el['equipment_id_id'])
        exercise = Exercises.objects.filter(equipment_id = equipment, muscle_id = muscle, difficulty = user_exp)
        if exercise.count() >= 1:
            for el2 in  exercise.values():
                exer = Exercises.objects.get(id = el2['id'])
                desc = el2['description']
                potential_workout.append({'exercise_id': exer, 'description': desc})
                

    if len(potential_workout) < 3:
        return Response("Nie udało się utworzyć treningu przy podanej specyfikacji!")

    new_workout = Workouts.objects.create(user_id = user_data, muscle_id = muscle, gym_id = gym, date = data['date'])
    i = 0

    random_indexes = list(range(len(potential_workout)))
    if len(potential_workout) > 5:
        random_exercises = random.sample(random_indexes, 5) #5 jest maksymalną ilością cwiczeń w zestawie
        for el in random_exercises:
            record = potential_workout[el]
            Workout_details.objects.create(workout_id = new_workout, exercise_id = record['exercise_id'], description = record['description'])
    else:
        for el in potential_workout:
            if i == 5:
                break
            Workout_details.objects.create(workout_id = new_workout, exercise_id = el['exercise_id'], description = el['description'])
            i+=1

    
    return Response("Trening został uwtorzony")
