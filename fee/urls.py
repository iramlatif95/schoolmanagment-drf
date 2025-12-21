from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import FeeStructureViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'fees', FeeStructureViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
