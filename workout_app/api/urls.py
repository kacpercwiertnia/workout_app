from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('muscles/', views.getMuscles, name="muscles"),
    path('user/', views.getUserProfile, name="user"),
    path('user/gyms/', views.getUserGyms, name="user_gyms"),
    path('user/gyms/all/', views.getAllUserGyms, name="user_gyms_all"),
    path('user/gyms/<int:pk>/', views.getUserGym, name="user_gym"),
    path('user/gyms/<int:pk>/update/', views.UpdateUserGym, name="user_gym_update"),
    path('user/gyms/<int:pk>/share/', views.ShareGym, name="share_gym"),
    path('user/gyms/create/', views.CreateUserGyms, name="user_gyms_info"),
    path('user/gyms/sharedlist/', views.GetSharedGyms, name="shared_gyms_list"),
    path('user/gyms/sharedlist/<int:pk>/', views.getPublicGymEqupiments, name="shared_gyms_equipments"),
    path('user/gyms/sharedlist/<int:pk>/addDelete/', views.addOrDeleteSharedGymToUserGyms, name="shared_gyms_add_delete"),
    path('user/gyms/sharedlist/<int:pk>/isAdded/', views.checkIfGymAdded, name="shared_gyms_check_added"),
    path('user/gyms/equipments/', views.getEquipments, name="user_gym_equipments"),
    path('user/gyms/<int:pk>/equipments/', views.getGymEqupiments, name="gym_equipments"),
    path('user/workouts/', views.getUserWorkouts, name="user_gyms"),
    path('user/workouts/<int:pk>/', views.getUserWorkout, name="user_workout"),
    path('user/workouts/<int:pk>/change/', views.changeExercise, name="change_exercise"),
    path('user/workouts/<int:pk>/changeWeight/', views.changeWeights, name="change_weight"),
    path('user/workouts/create/', views.CreateUserWorkout, name="user_workout_create"),
    path('user/<int:pk>/', views.UpdateUserView, name="user_update"),
]