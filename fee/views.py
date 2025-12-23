from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Fee, Payment
from .serializers import FeeSerializer, PaymentSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status 
from rest_framework.filters import SearchFilter 
from django_filters.rest_framework import DjangoFilterBackend

class FeeViewSet(viewsets.ModelViewSet):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['student', 'fee', 'status']
    search_fields = ['student__username']
    

    def get_queryset(self):
        user = self.request.user

        if user.role == 'admin':
            return Payment.objects.select_related('student', 'fee')

    
        if user.role == 'teacher':
            return Payment.objects.filter(
                fee__class_section__school_class__subject__teacher=user
            )


        if user.role == 'student':
            return Payment.objects.filter(student=user)

        return Payment.objects.none()

    def create(self, request, *args, **kwargs):
        student = request.data.get('student')
        fee = request.data.get('fee')

    
        if Payment.objects.filter(student=student, fee=fee).exists():
            return Response(
                {"error": "Payment already exists for this student and fee"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        payment = self.get_object()
        payment.delete()
        return Response(
            {"success": "Payment record deleted successfully"},
            status=status.HTTP_200_OK
        )


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['student', 'fee', 'status']
    search_fields = ['student__username']
    

    def get_queryset(self):
        user = self.request.user


        if user.role == 'admin':
            return Payment.objects.select_related('student', 'fee')

    
        if user.role == 'teacher':
            return Payment.objects.filter(
                fee__class_section__school_class__subject__teacher=user
            )

    
        if user.role == 'student':
            return Payment.objects.filter(student=user)

        return Payment.objects.none()

    def create(self, request, *args, **kwargs):
        student = request.data.get('student')
        fee = request.data.get('fee')

    
        if Payment.objects.filter(student=student, fee=fee).exists():
            return Response(
                {"error": "Payment already exists for this student and fee"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        payment = self.get_object()
        payment.delete()
        return Response(
            {"success": "Payment record deleted successfully"},
            status=status.HTTP_200_OK
        )

