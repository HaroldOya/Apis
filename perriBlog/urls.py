from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro', views.registro, name='registro'),
    path('perro', views.perri_list, name='perri_list'),
    path('perro/<int:pk>/edit/', views.perri_detail, name='perri_detail'),
]