from django.contrib import admin
from .models import Equipments
from .models import Muscles
from .models import Exercises
from .models import Users
from .models import Gyms
from .models import Shared_gyms
from .models import Workouts
from .models import Gym_details
from .models import Workout_details
# Register your models here.

admin.site.register(Equipments)
admin.site.register(Muscles)
admin.site.register(Exercises)
admin.site.register(Users)
admin.site.register(Gyms)
admin.site.register(Shared_gyms)
admin.site.register(Workouts)
admin.site.register(Gym_details)
admin.site.register(Workout_details)

