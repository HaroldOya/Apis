from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from perriblog import views
from perriblog.models import Perro

router = routers.DefaultRouter()
router.register(r'perros', views.PerroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url( r'^', include(router.urls)),
    url( r'^api-auth/', include( 'rest_framework.urls', namespace='rest_framework' ))
]
