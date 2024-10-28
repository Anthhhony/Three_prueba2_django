from django.db import models

class DBproyecto(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=30)
    telefono = models.IntegerField()
    edad = models.IntegerField()
    correo = models.EmailField()

# Create your models here.
