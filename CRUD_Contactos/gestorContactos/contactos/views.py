from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
def contactos_list(request):
    contactos = Contacto.objects.all()

    context = {
        'contactos': contactos
    }
    return render(request, 'index.html', context)

def contactos_create(request):
    form = ContactoModelForm()
    if request.method == 'POST':
        form = ContactoModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    context = {
        'form': form,
        'title': 'Añadir Contacto'
    }
    return render(request, 'contactos/create.html', context)