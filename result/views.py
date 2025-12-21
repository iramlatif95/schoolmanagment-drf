from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Exam, Result
from .serializers import ExamSerializer, ResultSerializer

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

# Create your views her