from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

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


    # used the filters  



# Create your views here.
