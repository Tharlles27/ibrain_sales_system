from rest_framework import viewsets
from .models import Diretoria
from .serializers import DiretoriaSerializer

class DiretoriaViewSet(viewsets.ModelViewSet):
    queryset = Diretoria.objects.all()
    serializer_class = DiretoriaSerializer
