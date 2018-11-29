from .models import Perro
from rest_framework import viewsets
from perriblog.serializers import PerroSerializers

class PerroViewSet( viewsets.ModelViewSet ):
    queryset = Perro.objects.all().order_by ( 'published_date')
    serializer_class = PerroSerializers