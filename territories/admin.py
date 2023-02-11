from django.contrib import admin
from .models import Diretoria, Unidade, Vendedor



class DiretoriaAdmin(admin.ModelAdmin):
    list_display = ['name', 'director']
    
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ['name', 'board', 'location', 'manager']


admin.site.register(Diretoria, DiretoriaAdmin)
admin.site.register(Unidade, UnidadeAdmin)
admin.site.register(Vendedor)