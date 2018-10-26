from django.db import models
from django.utils import timezone

# Create your models here.
class Perro(models.Model):
    Nombre = models.CharField(max_length=200)
    Raza = models.CharField(max_length=200)
    Descripcion = models.TextField(max_length=200)
    ESTADOS = (
        ('Rescatado', 'rescatado'),
        ('Disponible', 'disponible'),
        ('Adoptado', 'adoptado'),
    )
    Estado = models.CharField(max_length=20, choices=ESTADOS)
    
    publish_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.Nombre

class Cliente(models.Model):
    Correo = models.CharField(max_length=200)
    Rut = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=200)
    FechaNac = models.DateTimeField(blank=True, null=True)
    Telefono = models.IntegerField
    Region = models.CharField(max_length=200)
    Ciudad = models.CharField(max_length=200)
    Vivienda = models.CharField(max_length=200)


    def __str__(self):
        return self.Rut
