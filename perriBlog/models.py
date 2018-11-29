from django.db import models
from django.utils import timezone

# Create your models here.
class Perro (models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    detalle = models.CharField(max_length=300)
    imagen = models.CharField(max_length=200)
    ESTADOS = (
        ('Rescatado', 'rescatado'),
        ('Disponible', 'disponible'),
        ('Adoptado', 'adoptado'),
    )
    estado = models.CharField(max_length=20, choices=ESTADOS)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def Publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre
