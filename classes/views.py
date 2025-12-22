from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated 
from rest_framework_simplejwt.authentication import JWTAuthentication 
from.models import Class,Section
from .serializers import ClassSerializer, SectionSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    
    def get_queryset(self):
        user = self.request.user

        if user.role == 'admin':
            return Section.objects.all()
        elif user.role == 'teacher':
            return Section.objects.filter(
                school_class__subject__teacher=user
            ).distinct()
        elif user.role == 'student':
            return Section.objects.filter(
                enrollment__student=user
            )
        else:
            return Section.objects.none()

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy', 'partial_update']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    def destroy(self, request):
        class_obj = self.get_object()
        if class_obj.enrollment_set.exists():
            return Response({"error": "Cannot delete class with enrolled students"}, status=400)
        class_obj.delete()
        return Response({"success": "Class deleted"})
    
    @action(detail=True,methods=['get'])
    def sections(self,request,pk=None):
        class_object=self.get_object()
        serializer=SectionSerializer(class_object.sections.all(),many=True)
        return Response(serializer.data)

class SectionViewSet(viewsets.ModelViewSet):
    queryset=Section.objects.all()
    serializer_class=SectionSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.user()

        if user.role=='admin':
            return Section.objects.select_related('school_class')
        elif user.role=='teacher':
            return Section.objects.filter(
                school_class__subject__teacher=user
            ).distinct   
        elif user.role=='student':
            return Section.objects.filter(
                entrolment__student=user
            )
        return Section.objects.none()
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
    def create(self, request, *args, **kwargs):
        school_class = request.data.get('school_class')
        name = request.data.get('name')

    
        if Section.objects.filter(
            school_class_id=school_class,
            name=name
        ).exists():
            return Response(
                {"error": "Section already exists in this class"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)


# Create your views here.
