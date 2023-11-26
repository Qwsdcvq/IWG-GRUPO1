from django.db import models

# Create your models here.

class User(models.Model):
    nombre_usuario = models.CharField(max_length=30,unique=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50, default='')   
    puntos = models.IntegerField(default=100)
    last_login = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_usuario