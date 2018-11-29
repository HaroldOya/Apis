from .models import Perro
from rest_framework import serializers

class PerroSerializers ( serializers.HyperlinkedModelSerializer):
    author = serializers.CharField( source='author.username', read_only=True )
    class Meta:
        model = Perro
        fields = ('author','nombre', 'raza', 'detalle', 'imagen','estado', 'published_date')