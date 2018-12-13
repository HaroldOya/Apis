from .models import Oferta
from rest_framework import viewsets
from ofertasBlog.serializers import OfertaSerializers

class OfertaViewSet( viewsets.ModelViewSet ):
    queryset = Oferta.objects.all().order_by ( 'published_date')
    serializer_class = OfertaSerializers