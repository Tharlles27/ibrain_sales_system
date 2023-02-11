from django.urls import path, include
from rest_framework import routers
from .views import DiretoriaViewSet

router = routers.DefaultRouter()
router.register(r'diretorias', DiretoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
