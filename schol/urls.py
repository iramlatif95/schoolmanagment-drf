# school/urls.py
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, BranchViewSet

router = DefaultRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'branches', BranchViewSet)

urlpatterns = router.urls
