from django.db import models

# Create your models here.

class User(models.Model):
    nombre_usuario = models.CharField(max_length=30,unique=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    patente = models.CharField(max_length=9, default='', blank=True)
    puntos = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre_usuario