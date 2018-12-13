from django.db import models
from django.utils import timezone

# Create your models here.
class Oferta (models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    precio = models.CharField(max_length=20)
    producto = models.CharField(max_length=300)
    imagen = models.CharField(max_length=200)
    oferta = models.CharField(max_length=20)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def Publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre
