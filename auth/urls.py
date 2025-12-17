from rest_framework.routers import DefaultRouter 
from . views import UserViewSets, viewsets 
from django.urls import path, include

router=DefaultRouter()
router.register(r'user',UserViewSets)

urlpatterns = [
    path('', include(router.urls)),
]



#urlpatterns = router.urls
