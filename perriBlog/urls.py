from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('registro', views.registro, name='registro'),
    path('perro', views.perri_list, name='perri_list'),
    path('perro/new', views.perro_new, name='perro_new'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)