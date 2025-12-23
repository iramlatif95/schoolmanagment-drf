from django.shortcuts import render
# school/views.py
from rest_framework.viewsets import ModelViewSet
from .models import School, Branch
from .serializers import SchoolSerializer, BranchSerializer
from rest_framework.response import Response
from rest_framework.filters import SearchFilter 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status

class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', 'email']
    

    def get_queryset(self):
        user = self.request.user

    
        if user.role == 'admin':
            return School.objects.all()

    
        return School.objects.all()

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')


        if School.objects.filter(email=email).exists():
            return Response(
                {"error": "School with this email already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        school = self.get_object()

        if school.branches.exists():
            return Response(
                {"error": "Cannot delete school with existing branches"},
                status=status.HTTP_400_BAD_REQUEST
            )

        school.delete()
        return Response({"success": "School deleted successfully"})
class BranchViewSet(ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['school', 'city', 'is_active']
    search_fields = ['name', 'city']
   

    def get_queryset(self):
        user = self.request.user

        
        if user.role == 'admin':
            return Branch.objects.select_related('school')

    
        return Branch.objects.filter(is_active=True).select_related('school')

    def create(self, request, *args, **kwargs):
        school = request.data.get('school')
        name = request.data.get('name')

    
        if Branch.objects.filter(school=school, name=name).exists():
            return Response(
                {"error": "Branch already exists for this school"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        branch = self.get_object()

    
        if not branch.is_active:
            return Response(
                {"error": "Branch is already inactive"},
                status=status.HTTP_400_BAD_REQUEST
            )

        branch.delete()
        return Response({"success": "Branch deleted successfully"})



# Create your views here.
