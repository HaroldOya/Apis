from django.shortcuts import render
from django.utils import timezone
from .models import Perro
from .models import Cliente
from django.shortcuts import render, get_object_or_404
from .forms import PerroForm
from django.shortcuts import redirect

# Create your views here.
def perri_list(request):
    
    perro = Perro.objects.order_by('Estado')
    return render(request, 'MisPerris/perri_list.html', {'perro': perro})
def listar(request):
    perros_adoptados = Perro.objects.filter(Estado='Adoptado')
    perros_rescatado = Perro.objects.filter(Estado='Rescatado')
    perros_disponible = Perro.objects.filter(Estado='Disponible')
    context = {'perros_adoptados': perros_adoptados,
               'perros_rescatado': perros_rescatado,
               'perros_disponible': perros_disponible}
    return render(request, 'MisPerris/perri_list.html',context)

def index(request):
    return render(request, 'MisPerris/index.html')

def registro(request):
    return render(request, 'MisPerris/registro.html') 
 

def perro_new(request):
    if request.method == "PERRO":
        form = PerroForm(request.PERRO)
        if form.is_valid():
            perro = form.save(commit=False)
            perro.save()
            
    else:
        form = PerroForm()
    return render(request, 'MisPerris/perri_edit.html', {'form': form})




