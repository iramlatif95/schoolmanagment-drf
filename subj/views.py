from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter 
from rest_framework.response import Response 

from .models import Subject
from .serializers import SubjectSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # Filters and search
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['branch', 'class_obj', 'teacher']  
    search_fields = ['name'] 
    

    def get_queryset(self):
        user = self.request.user

    
        if user.role == 'admin':
            return Subject.objects.select_related(
                'branch', 'class_obj', 'teacher'
            )

        
        if user.role == 'teacher':
            return Subject.objects.filter(
                teacher=user
            ).select_related('branch', 'class_obj')

    
        if user.role == 'student':
            return Subject.objects.filter(
                class_obj__section__enrollment__student=user
            ).distinct()

        return Subject.objects.none()
    
    def create(self, request, *args, **kwargs):
                name = request.data.get('name')
                class_obj = request.data.get('class_obj')
                branch = request.data.get('branch')

        # Business rule: same subject should not repeat
                if Subject.objects.filter(
                            name=name,
                            class_obj=class_obj,
                            branch=branch
                        ).exists():
                        return Response(
                        {"error": "Subject already exists for this class and branch"},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                return super().create(request, *args, **kwargs)





    # used the filters  



# Create your views here.
