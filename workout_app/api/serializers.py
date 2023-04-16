from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError
from django.contrib.auth.models import User
from .models import Users
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
        fields = ('age', 'height', 'weight', 'experience', 'user')
    
    def update(self, instance, validated_data):
        user_to_update = Users.objects.get(user = 'user')
        print('age')

        #user_to_update.age = 'age'
        #user_to_update.height = 'height'
        #user_to_update.weight = 'weight'
        #user_to_update.experience = 'experience'

        #user_to_update.save()

        #return user_to_update

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'