from django.shortcuts import render
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from profileapp.models import Profile
from profileapp.serializers import ProfileSerializer

class ProfileCreateAPIView(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
