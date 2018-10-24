from django.db import models
from django.utils import timezone

# Create your models here.
class Perro(models.Model):
    Nombre = models.CharField(max_length=200)
    Raza = models.CharField(max_length=200)
    Descripcion = models.TextField(max_length=200)
    Estado = models.CharField(max_length=200)
    publish_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.Nombre

class Cliente(models.Model):
    Rut = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=200)
    FechaNac = models.DateTimeField(blank=True, null=True)
    Telefono = models.IntegerField
    publish_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.Rut
