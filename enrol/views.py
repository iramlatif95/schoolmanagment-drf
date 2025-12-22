from django.shortcuts import render

from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated
from .models import Enrollment
from .serializers import EnrollmentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['class_section', 'student']
    search_fields = ['student__username', 'class_section__name']

    def get_queryset(self):
        user=self.request.user

        if user.role=='admin':
            return Enrollment.objects.select_related('student','class_section') # f-k 
        elif user.role=='teacher':
            return Enrollment.objects.filter(
                class_section__school_class__subject__teacher=user
            ).select_related('student', 'class_section')

        elif user.role == 'student':
            return Enrollment.objects.filter(student=user)

        return Enrollment.objects.none()
    

    def get_permissions(self):
        # Only admin can create/update/delete enrollments
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
    def create(self, request, *args, **kwargs):
        student = request.data.get('student')
        class_section = request.data.get('class_section')
    
    
        if Enrollment.objects.filter(student=student, class_section=class_section).exists():
            return Response(
                {'error': 'Student is already enrolled in this class section'},
                status=status.HTTP_400_BAD_REQUEST
        )
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        enrollment=self.get_object()
        enrollment.delete()
        return Response(
            {"success": "Enrollment deleted successfully"},
            status=status.HTTP_200_OK
        )
        
        
        





# Create your views here.
