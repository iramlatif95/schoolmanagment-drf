from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet

router = DefaultRouter()
router.register(r'subject', SubjectViewSet)

urlpatterns = router.urls
