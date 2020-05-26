from django.shortcuts import render
from .serializers import  RegisterUserSerializer
# Create your views here.

class RegisterView():
    serializer = RegisterUserSerializer
    