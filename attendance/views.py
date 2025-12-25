from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Attendance
from .serializers import AttendanceSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import BasePermission


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
    #permission_classes = [IsAuthenticated, IsAdminOrTeacher]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['student', 'class_section', 'date', 'status']
    search_fields = ['student__username', 'class_section__name']

    def get_queryset(self):
        user = self.request.user


        if user.role == 'admin':
            return Attendance.objects.select_related('student', 'class_section')

    
        if user.role == 'teacher':
            return Attendance.objects.filter(
                class_section__school_class__subject__teacher=user
            ).select_related('student', 'class_section')

        
        if user.role == 'student':
            return Attendance.objects.filter(student=user)

        return Attendance.objects.none()


class IsAdminOrTeacher(BasePermission):

    def has_permission(self, request, view):
        
        if view.action in ['list', 'retrieve']:
            return True
        
       
        if request.user.role == 'admin':
            return True
        
    
        if request.user.role == 'teacher':
            return view.action in ['create', 'update', 'partial_update']
        
    
        return False
    
    def create(self, request, *args, **kwargs):
        student = request.data.get('student')
        date = request.data.get('date')
        class_section = request.data.get('class_section')

        # Prevent duplicate attendance entry for same student, date, section
        if Attendance.objects.filter(
            student=student,
            date=date,
            class_section=class_section
        ).exists():
            return Response(
                {"error": "Attendance already marked for this student on this date and section"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        attendance = self.get_object()
        attendance.delete()
        return Response(
            {"success": "Attendance record deleted successfully"},
            status=status.HTTP_200_OK
        )



    


# Create your views here.
