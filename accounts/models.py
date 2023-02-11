from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class CustomUserManager(BaseUserManager):
    """
    Gerenciador de modelo de usuário personalizado em que o e-mail é o identificador exclusivo
    para autenticação em vez de nomes de usuários.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Crie e salve um usuário com o e-mail e a senha fornecidos.
        """
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Crie e salve um SuperUser com o e-mail e a senha fornecidos.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    
    #Padronizei o uuid como id (dificulta bruteforce em enumeração de uauários)
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
        )
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}"
    


class Cargo(models.Model):
    CARGO_CHOICES = (
        ("Diretor Geral", "Diretor Geral"),
        ("Diretor", "Diretor"),
        ("Gerente", "Gerente"),
        ("Vendedor", "Vendedor"),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=20, verbose_name="Cargo", choices=CARGO_CHOICES)
    
    def __str__(self):
        return f"{self.nome}"