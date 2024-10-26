from django.shortcuts import render

# Create your views here.
def contactos_list(request):
    return render(request, 'index.html')