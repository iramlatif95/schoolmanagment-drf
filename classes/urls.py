from rest_framework.routers import DefaultRouter
from .views import ClassViewSet, SectionViewSet

router = DefaultRouter()
router.register(r'classes', ClassViewSet)
router.register(r'sections', SectionViewSet)

urlpatterns = router.urls
