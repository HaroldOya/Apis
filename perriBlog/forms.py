from django import forms

from .models import Perro
from .models import Cliente

class PerroForm(forms.ModelForm):

    class Meta:
        model = Perro
        fields = ('Nombre', 'Raza','Descripcion','Estado','Imagen',)

