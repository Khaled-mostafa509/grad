from django.shortcuts import render
from .serializers import PersonCustomRegistrationSerializer, CompanyCustomRegistrationSerializer 
from rest_framework.generics import GenericAPIView
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

# class PersonRegistrationView(RegisterView):
#     serializer_class = PersonCustomRegistrationSerializer
class PersonRegistrationView(GenericAPIView):
    serializer_class = PersonCustomRegistrationSerializer
    
    def post(self,request):
        serializer =self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   

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
class CompanyRegistrationView(GenericAPIView):
    serializer_class = CompanyCustomRegistrationSerializer
    
    def post(self,request):
        serializer =self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)