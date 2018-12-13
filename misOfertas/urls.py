from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from ofertasBlog import views
from ofertasBlog.models import Oferta

router = routers.DefaultRouter()
router.register(r'ofertas', views.OfertaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url( r'^', include(router.urls)),
    url( r'^api-auth/', include( 'rest_framework.urls', namespace='rest_framework' ))
]
