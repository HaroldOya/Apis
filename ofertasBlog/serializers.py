from .models import Oferta
from rest_framework import serializers

class OfertaSerializers ( serializers.HyperlinkedModelSerializer):
    author = serializers.CharField( source='author.username', read_only=True )
    class Meta:
        model = Oferta
        fields = ('author','nombre', 'precio', 'producto', 'imagen','oferta', 'published_date')