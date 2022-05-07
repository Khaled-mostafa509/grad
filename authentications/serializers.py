from django.db import models
from rest_framework import serializers ,permissions
# from rest_auth.registration.serializers import RegisterSerializer 
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate , login
from .models import Person,Company

class PersonCustomRegistrationSerializer(serializers.ModelSerializer):
    person = serializers.PrimaryKeyRelatedField(read_only=True,)
    first_name = models.CharField( )
    last_name = models.CharField( )
    phone_number = models.CharField()
    image = models.ImageField( )

    
    def get_cleaned_data(self):
            data = super(PersonCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'first_name' : self.validated_data.get('first_name', ''),
                'last_name' : self.validated_data.get('last_name', ''),
                'phone_number': self.validated_data.get('phone_number', ''),
                'image': self.validated_data.get('image', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(PersonCustomRegistrationSerializer, self).save(request)
        user.is_person = True
        user.save()
        person = Person(person=user, first_name=self.cleaned_data.get('first_name'), 
                last_name=self.cleaned_data.get('last_name'),
                phone_number=self.cleaned_data.get('phone_number'),
                image=self.cleaned_data.get('image'))
        person.save()
        return user

class LoginSerializers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6 , write_only=True) 
    class Meta:
        
        model= User
        fields = ('email','password','token')
        read_only_fields = ['token']
# class loginSerializer(KnoxLoginView):
#     permissions_classes = (permissions.AllowAny,)
    
    
#     def post(self,request,format=None):
#         serializer=AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception = True)
#         user = serializer.validated_data['user']
#         login(request,user)
#         return super(loginSerializer,self).post(request,format=None)
        # if request.method == "POST":
        #     username = request.POST['username']
        #     password = request.POST['password']
        #     seo_specialist = authenticate(username=username, password=password)
        #     if seo_specialist is not None:
        #         return HttpResponse("Signed in")
        #     else:
        #         return HttpResponse("Not signed in")




class CompanyCustomRegistrationSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(read_only=True,)
    company_name = serializers.CharField()
    phone_number = serializers.CharField()
    logo = serializers.ImageField()
    
    def get_cleaned_data(self):
            data = super(CompanyCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'company_name' : self.validated_data.get('company_name', ''),
                'phone_number' : self.validated_data.get('phone_number', ''),
                'logo' : self.validated_data.get('logo', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(CompanyCustomRegistrationSerializer, self).save(request)
        user.is_company = True
        user.save()
        company = Company(company=user,company_name=self.cleaned_data.get('company_name'),phone_number=self.cleaned_data.get('phone_number'),logo=self.cleaned_data.get('logo'))
        company.save()
        return user