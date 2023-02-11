# serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Produto, Venda
from accounts.models import User


User = get_user_model()

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
        
class VendaSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(write_only=True)

    class Meta:
        model = Venda
        fields = ('id', 'user', 'user_email', 'produto', 'quantidade')
        read_only_fields = ('id',)

    def create(self, validated_data):
        user_email = validated_data.pop('user_email')
        user = User.objects.get(email=user_email)
        validated_data['user'] = user
        return super().create(validated_data)