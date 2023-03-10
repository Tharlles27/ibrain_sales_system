# Generated by Django 4.1.6 on 2023-02-10 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('territories', '0003_unidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidade',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unidade_seller', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unidade_manager', to=settings.AUTH_USER_MODEL),
        ),
    ]
