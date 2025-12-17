from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.permissions import IsAdminUser 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework import status
from .models import School, Branch
from .serializers import Schoolserializer,Branchserializer  

class SchoolViewSet(viewsets.ModelViewSet):
    queryset=School.objects.all()
    serializer_class=Schoolserializer 
    permission_classes=[IsAdminUser]

class BranchViewSet(viewsets.ModelViewSet):
    queryset=Branch.objects.all()
    serializer_class=Branchserializer 
    permission_classes=[IsAdminUser]



# Create your views here.
