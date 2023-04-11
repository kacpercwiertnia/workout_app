from rest_framework.serializers import ModelSerializer
from .models import Muscles

class MusclesSerializer(ModelSerializer):
    class Meta:
        model = Muscles
        fields = '__all__'