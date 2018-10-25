from django.shortcuts import render
from django.utils import timezone
from .models import Perro
from .models import Cliente
from django.shortcuts import render, get_object_or_404

# Create your views here.
def perri_list(request):
    
    perro = Perro.objects.order_by('Estado')
    return render(request, 'MisPerris/perri_list.html', {'perro': perro})

def perri_detail(request, pk):
    perro = get_object_or_404(Perro, pk=pk)
    return render(request, 'MisPerris/perri_detail.html', {'perro': perro})

def index(request):
    return render(request, 'MisPerris/index.html')

def registro(request):
    return render(request, 'MisPerris/registro.html')    


