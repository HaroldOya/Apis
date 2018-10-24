from django.shortcuts import render

# Create your views here.
def perri_list(request):
    return render(request, 'MisPerris/perri_list.html', {})
