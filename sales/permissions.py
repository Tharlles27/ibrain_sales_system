# permissions.py
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

def create_add_venda_permission(model_class):
    content_type = ContentType.objects.get_for_model(model_class)
    permission, created = Permission.objects.get_or_create(
        codename='add_venda',
        content_type=content_type,
        defaults={'name': 'Can add Venda'},
    )
    return permission
