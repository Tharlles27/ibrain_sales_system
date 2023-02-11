from django.db import models
from django.conf import settings


#Class de diretoria
class Diretoria(models.Model):
    director = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20, verbose_name="Diretoria")
    
    def __str__(self):
        return self.name

#Class de unidade
class Unidade(models.Model):
    board = models.ForeignKey(Diretoria, on_delete=models.SET_NULL, null=True) # Diretoria
    manager = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True,
    related_name='unidade_manager'
    )
    name = models.CharField(max_length=30, verbose_name="Unidade")
    location = models.CharField(max_length=150, verbose_name="Coordenadas", null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
    
class Vendedor(models.Model):
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='unidade_seller'
    )
    unidade = models.ForeignKey(
        Unidade,
        on_delete=models.SET_NULL,
        null=True
    )
    def __str__(self):
        return f"{self.seller} - {self.unidade}"