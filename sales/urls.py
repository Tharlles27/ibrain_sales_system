from django.urls import path, include
from rest_framework import routers
from .views import ProdutoViewSet, SalesView

router = routers.DefaultRouter()
router.register(r'products', ProdutoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('vendas/<str:pk>/', SalesView.as_view(), name='user-detail'),
]