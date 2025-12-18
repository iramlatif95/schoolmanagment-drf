from django.shortcuts import render
# school/views.py
from rest_framework.viewsets import ModelViewSet
from .models import School, Branch
from .serializers import SchoolSerializer, BranchSerializer

class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
class BranchViewSet(ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


# Create your views here.
