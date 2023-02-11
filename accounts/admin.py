from django.contrib import admin
from accounts.models import User, Cargo
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email']
    
class CargoAdmin(admin.ModelAdmin):
    list_display = ['user', 'nome']

admin.site.register(User, UserAdmin)
admin.site.register(Cargo, CargoAdmin)