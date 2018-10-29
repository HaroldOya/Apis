from django.forms import ModelForm
from django import forms
from .models import Perro
from .models import Cliente

class PerroForm(forms.ModelForm):

    class Meta:
        model = Perro
        fields = ('Nombre', 'Raza','Descripcion','Estado','Imagen')
        widgets = {
            'Descripcion': forms.TextInput(attrs={'class':'Formulario'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('Correo', 'Rut','Nombre','FechaNac','Telefono','Region','Ciudad','Vivienda')
        widgets = {
            'Nombre': forms.TextInput(attrs={'class':'form'}),
            'Rut': forms.TextInput(attrs={'class':'Form'}),
            'FechaNac': forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'Form','placeholder':'MM/DD/YYYY'}),
            'Correo': forms.EmailInput(attrs={'class':'Form','placeholder':'Ingrese correo'}),
            'Telefono': forms.TextInput(attrs={'class':'Form','type':'number'}),
        }


   
