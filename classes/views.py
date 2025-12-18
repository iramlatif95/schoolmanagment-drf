from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated 
from rest_framework_simplejwt.authentication import JWTAuthentication 
from.models import Class,Section

from .serializers import ClassSerializer, SectionSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset=Class.objects.all()
    serializer_class=ClassSerializer 
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

class SectionViewSet(viewsets.ModelViewSet):
    queryset=Section.objects.all()
    serializer_class=SectionSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]


# Create your views here.
