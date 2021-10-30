from django.shortcuts import render
from rest_framework import generics  # <- import generics
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import permissions
from messenger.permissions import IsOwnerOrReadOnly
# Create your views here.




class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    # add code here
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_fields = 'username'
   
