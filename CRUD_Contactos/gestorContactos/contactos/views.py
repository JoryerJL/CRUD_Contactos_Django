from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
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
            form = ContactoModelForm()
        else:
            print(form.errors)

    context = {
        'form': form,
        'title': 'Añadir Contacto'
    }
    return render(request, 'contactos/create.html', context)

def contactos_delete(request, pk):
    Contacto.objects.get(pk=pk).delete()
    return redirect(contactos_list)

def contactos_edit(request, pk):
    contacto = Contacto.objects.get(pk=pk)
    form = ContactoModelForm(instance=contacto)
    if request.method == 'POST':
        form = ContactoModelForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect(contactos_list)
        else:
            print(form.errors)

    context = {
        'form': form,
    }
    return render(request, 'contactos/create.html', context)