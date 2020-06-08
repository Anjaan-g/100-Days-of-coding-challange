from django.shortcuts import render
from .serializers import  RegisterUserSerializer, UserSerializer, ProfileSerializer
from rest_framework import viewsets, generics, permissions, status
from .models import CustomUser, UserProfile
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.views import APIView
# Create your views here.

class UserView(viewsets.ModelViewSet):
    model = CustomUser
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes_by_action = {
        'create': [AllowAny], ## Anyone can register ####
        'list': [AllowAny], #### TO list all users without login for now ####
    }
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

# class RegisterView(viewsets.ModelViewSet):
#     serializer = RegisterUserSerializer

class UserProfileView(viewsets.ModelViewSet):
    model = UserProfile
    serializer_class = ProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes_by_action = {
        'create': [AllowAny], ## Anyone can register ####
        'list': [AllowAny], #### TO list all users without login for now ####
    }

class LoginView(APIView):
    pass