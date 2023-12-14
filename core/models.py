from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, null=True)