from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated 
from .models import Subject 
from rest_framework_simplejwt.authentication import JWTAuthentication 
from .serializers import SubjectSerialzer  
#from rest_framework import filters

class SubjectViewSet(viewsets.ModelViewSet):
    queryset=Subject.objects.all()
    serializer_class=SubjectSerialzer 
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    # used the filters  qw add the filters bakends 
    filterset_fields = ['branch', 'class_obj', 'teacher'] 
    #filter_backends = [filters.SearchFilter]
    #search_fields = ['name']



    # used the filters  



# Create your views here.
