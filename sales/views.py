# views.py
from .serializers import ProdutoSerializer, VendaSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Produto, Venda
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from accounts.models import User


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
    
    
          
class SalesView(APIView):

    """
    Retrieve, update or delete a person instance.
    """

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        vendas = Venda.objects.filter(user=user)
        serializer = VendaSerializer(vendas, many=True)
        return Response(serializer.data)