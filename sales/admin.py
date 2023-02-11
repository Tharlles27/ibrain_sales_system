# admin.py
from django.contrib import admin
from .models import Produto, Venda

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'preco', 'estoque']



class VendaAdmin(admin.ModelAdmin):
    list_display = ['produto', 'quantidade']
    
    
    
    
    
    
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Venda, VendaAdmin)