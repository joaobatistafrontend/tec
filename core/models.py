from django.db import models

class Agendamento(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=30, default='')
    email = models.EmailField(max_length=100)
    opcoes = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    data = models.DateField()
    protocolo = models.CharField(max_length=100, unique=True, null=True, blank=True)
