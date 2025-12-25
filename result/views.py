from django.shortcuts import render


from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Exam, Result
from .serializers import ExamSerializer, ResultSerializer
from rest_framework.response import Response
from rest_framework.filters import SearchFilter 
from django_filters.rest_framework import DjangoFilterBackend

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['section', 'date']
    search_fields = ['name', 'section__name']
   

    def get_queryset(self):
        user = self.request.user

    
        if user.role == 'admin':
            return Exam.objects.select_related('section')

    
        if user.role == 'teacher':
            return Exam.objects.filter(
                section__school_class__subject__teacher=user
            )

        
        if user.role == 'student':
            return Exam.objects.filter(
                section__enrollment__student=user
            ).distinct()

        return Exam.objects.none()

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        section = request.data.get('section')
        date = request.data.get('date')

    
        if Exam.objects.filter(name=name, section=section, date=date).exists():
            return Response(
                {"error": "Exam already exists for this section on this date"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['section', 'date']
    search_fields = ['name', 'section__name']
    

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Exam.objects.select_related('section')

    
        if user.role == 'teacher':
            return Exam.objects.filter(
                section__school_class__subject__teacher=user
            )

        
        if user.role == 'student':
            return Exam.objects.filter(
                section__enrollment__student=user
            ).distinct()

        return Exam.objects.none()

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        section = request.data.get('section')
        date = request.data.get('date')

        
        if Exam.objects.filter(name=name, section=section, date=date).exists():
            return Response(
                {"error": "Exam already exists for this section on this date"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)

# Create your views her