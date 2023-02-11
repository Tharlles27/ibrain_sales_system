from rest_framework import serializers
from .models import Diretoria

class DiretoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diretoria
        fields = ('id', 'director', 'name')
