from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from.models import *


# Create your views here.
def contactos_list(request):
    contactos = Contacto.objects.all()

    context = {
        'contactos': contactos
    }
    return render(request, 'index.html', context)