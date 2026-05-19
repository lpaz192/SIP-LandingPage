from django.contrib.auth.models import User
from django.db import models

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, default='')

    class Meta:
        db_table = 'clientes'

class Soporte(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, default='')
    empresa = models.CharField(max_length=100, default='')

    class Meta:
        db_table = 'soporte'

class JefeSoporte(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, default='')
    empresa = models.CharField(max_length=100, default='')

    class Meta:
        db_table = 'jefes_soporte'