from django.db import models
from django.contrib.auth.models import User

OPTIONS = [
    ('DEBUG', 'DEBUG'),
    ('ERROR', 'ERROR'),
    ('WARNING', 'WARNING'),
]

class Level(models.Model):
    description = models.TextField("Descrição", max_length=8, choices=OPTIONS)

class Origin(models.Model):
    description = models.TextField("Descrição", max_length=500)

class Environment(models.Model):
    description = models.CharField("Descrição", max_length=50)

class Log(models.Model):
    details = models.TextField("Detalhes", max_length=500)
    number_events = models.IntegerField("Quantidade de Eventos")
    occurrence_date = models.DateTimeField("Data de Ocorrência", auto_now_add=True)
    title = models.CharField("Título", max_length=100)
    active = models.BooleanField("Ativo", default=True)
    environment = models.ForeignKey(Environment, on_delete=models.PROTECT, null=True)
    level = models.ForeignKey(Level, on_delete=models.PROTECT, null=True)
    origin = models.ForeignKey(Origin, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
