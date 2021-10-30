from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('messenger/', views.PostHistory.as_view(), name='post_history'),
    path('messenger/<int:pk>',
         views.PostDetail.as_view(), name='post_detail'),
]
