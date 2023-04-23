from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError
from django.contrib.auth.models import User
from .models import Users
from .models import Gyms
from .models import Workouts
from .models import Muscles

class MusclesSerializer(ModelSerializer):
    class Meta:
        model = Muscles
        fields = '__all__'

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise ValidationError(
                {'email': "User with this email already exists."}
            )
        return attrs

    def create(self, validated_data):
        new_user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email']
        )

        new_user.set_password(validated_data['password'])
        new_user.save()

        new_user2 = Users.objects.create(
            user = new_user
        )

        new_user2.save()

        return new_user

class UpdateUserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'age', 'height', 'weight', 'experience')
    
    def update(self, instance, validated_data):
        instance.age = validated_data.get('age', instance.age)
        instance.height = validated_data.get('height', instance.height)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.experience = validated_data.get('experience', instance.experience)

        instance.save()

        return instance

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class UserGymSerializer(ModelSerializer):
    class Meta:
        model = Gyms
        fields = '__all__'

class UserWorkoutSerializer(ModelSerializer):
    class Meta:
        model = Workouts
        fields = '__all__'