from django.shortcuts import render
from django.utils import timezone
from .models import Perro
from .models import Cliente
from django.shortcuts import render, get_object_or_404
from .forms import PerroForm
from django.shortcuts import redirect

# Create your views here.
def perri_list(request):
    perros = Perro.objects.order_by('Estado')     
    perros_adoptados = Perro.objects.filter(Estado='Adoptado')
    perros_rescatado = Perro.objects.filter(Estado='Rescatado')
    perros_disponible = Perro.objects.filter(Estado='Disponible')
    context = {'perros_adoptados': perros_adoptados,
               'perros_rescatado': perros_rescatado,
               'perros_disponible': perros_disponible}
    return render(request, 'MisPerris/perri_list.html', context, { 'perros': perros } )

def index(request):
    return render(request, 'MisPerris/index.html')

def registro(request):
    return render(request, 'MisPerris/registro.html') 
 
def perro_detail(request, pk):
    perro = get_object_or_404(Perro, pk=pk)
    return render(request, 'MisPerris/perro_detail.html', { 'perro': perro })

def perro_new(request):
    if request.method == "POST":
        form = PerroForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            perro = form.save(commit=False)
            perro.published_date = timezone.now()
            perro.save()
              
    else:
        form = PerroForm()
    return render(request, 'MisPerris/perri_edit.html', {'form': form})

def perro_edit(request, pk):
    perro = get_object_or_404(Perro, pk=pk)
    if request.method == "POST":
        form = PerroForm(request.POST, instance=perro)
        if form.is_valid():
            perro = form.save(commit=False)
            perro.published_date = timezone.now()
            perro.save()
            return redirect('perro_detail', pk=perro.pk)
    else:
        form = PerroForm(instance=perro)
    return render(request, 'MisPerris/perri_edit.html', {'form': form})


