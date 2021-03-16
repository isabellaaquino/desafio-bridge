from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NumberForm
from .models import Number
# Create your views here.

def createEntradas(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/resultado/')
        
    else:
        form = NumberForm
        return render(request, "home.html", {'form': form})

def viewEntradas(request):
    obj = Number.objects.last()
    
    numbers = [obj.n1,obj.n2] 
    obj.n1=min(numbers)
    obj.n2=max(numbers)
    cont = 0
    for i in range(obj.n1+1,obj.n2):
        for c in range(2,i):
            if i%c==0:
                cont+=1
        if cont==0:
            if i > 1:
                obj.primos.append(i)
        cont = 0
    obj.save(update_fields=['primos'])
            

    context = {
        'n1': obj.n1,
        'n2': obj.n2,
        'primos': obj.primos
    }
    
    return render(request, "resultado.html", context)


def viewAll(request):
    allNumbers = Number.objects.all()
        
    context = {
        'allNumbers': allNumbers
    }
    
    return render(request, "historico.html", context)

