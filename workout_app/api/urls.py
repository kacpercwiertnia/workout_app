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
    path('user/workouts/', views.getUserWorkouts, name="user_gyms"),
    path('user/<int:pk>/', views.UpdateUserView, name="user_update"),
]