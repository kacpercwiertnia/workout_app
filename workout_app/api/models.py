from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# Create your models here.

def validate_difficulty(value):
    if value != 'B' and value != 'I' and value != 'A':
        raise ValidationError(
            _("difficulty %(value)s need to be B, I or A"),
            params={"value": value},
        )

def validate_age(value):
    if value < 15 or value > 100:
        raise ValidationError(
            _("age %(value)s need to be between 15 and 100"),
            params={"value": value},
        )

def validate_height(value):
    if value < 100 or value > 260:
        raise ValidationError(
            _("height %(value)s need to be between 100 and 260"),
            params={"value": value},
        )
    
def validate_weight(value):
    if value < 40 or value > 200:
        raise ValidationError(
            _("weight %(value)s need to be between 40 and 200"),
            params={"value": value},
        )

def validate_quantity(value):
    if value < 0:
        raise ValidationError(
            _("quantity %(value)s need to grater than 0"),
            params={"value": value},
        )

class Equipments(models.Model):
    equipment_name = models.TextField(max_length=100)

    def __str__(self):
        return self.equipment_name

class Muscles(models.Model):
    muscle_name = models.TextField(max_length=100)

    def __str__(self):
        return self.muscle_name

class Exercises(models.Model):
    exercise_name = models.TextField(max_length=100)
    muscle_id = models.ForeignKey(Muscles, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=1, validators=[validate_difficulty])
    equipment_id = models.ForeignKey(Equipments, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.exercise_name

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, validators=[validate_age])
    height = models.IntegerField(null=True, validators=[validate_height])
    weight = models.IntegerField(null=True, validators=[validate_weight])
    experience = models.CharField(null=True, max_length=1, validators=[validate_difficulty])

    def __str__(self):
        return self.user.username

class Gyms(models.Model):
    gym_name = models.TextField(max_length=255)
    address = models.TextField(max_length=255)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    is_shared = models.BooleanField(default=False)

    def __str__(self):
        return self.gym_name + " " + self.address

class Shared_gyms(models.Model):
    gym_id = models.ForeignKey(Gyms, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

class Workouts(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    muscle_id = models.ForeignKey(Muscles, on_delete=models.CASCADE, null=True)
    gym_id = models.ForeignKey(Gyms, on_delete=models.CASCADE, null=True)
    date = models.DateField()

class Gym_details(models.Model):
    gym_id = models.ForeignKey(Gyms, on_delete=models.CASCADE)
    equipment_id = models.ForeignKey(Equipments, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[validate_quantity])

class Workout_details(models.Model):
    workout_id = models.ForeignKey(Workouts, on_delete=models.CASCADE)
    exercise_id = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)