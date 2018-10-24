from django.urls import path
from . import views

urlpatterns = [
    path('', views.perri_list, name='perri_list'),
]