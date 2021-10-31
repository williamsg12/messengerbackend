from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('profile/', views.ProfileDetails.as_view(), name='profile_details'),

]
