from django.shortcuts import render
# from rest_auth.registration.views import RegisterView
from .serializers import PersonCustomRegistrationSerializer, CompanyCustomRegistrationSerializer 
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from rest_framework import permissions,generics
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class PersonRegistrationView(generics.GenericAPIView):
    serializer_class = PersonCustomRegistrationSerializer
    def post(self,request,*args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"account created successfully"
        })
    
class CompanyRegistrationView(generics.GenericAPIView):
    serializer_class = CompanyCustomRegistrationSerializer
    def post(self,request,*args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"account created successfully"
        })



class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

# class CompanyRegistrationView(RegisterView):
#     serializer_class = CompanyCustomRegistrationSerializer