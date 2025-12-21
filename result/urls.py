from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ExamViewSet, ResultViewSet

router = DefaultRouter()
router.register(r'exams', ExamViewSet)
router.register(r'results', ResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
