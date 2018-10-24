from django.shortcuts import render
from django.utils import timezone
from .models import Perro
from .models import Cliente

# Create your views here.
def perri_list(request):
    perro = Perro.objects.order_by('Estado')
    return render(request, 'MisPerris/perri_list.html', {'perro': perro})
