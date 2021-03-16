from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def result_view(request, *args, **kwargs):
    return render(request, 'resultado.html', {})

def hist_view(request, *ars, **kwargs):
    return render(request, 'historico.html', {})
