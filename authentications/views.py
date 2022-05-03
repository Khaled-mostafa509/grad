from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from .serializers import PersonCustomRegistrationSerializer, CompanyCustomRegistrationSerializer 
    
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class PersonRegistrationView(RegisterView):
    serializer_class = PersonCustomRegistrationSerializer
    

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class CompanyRegistrationView(RegisterView):
    serializer_class = CompanyCustomRegistrationSerializer