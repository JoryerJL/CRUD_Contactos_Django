from .views import *
from django.urls import path, include

urlpatterns = [
    path('', contactos_list, name = 'contactos_list'),
    path('crear/', contactos_create, name = 'crear'),
    path('borrar/<int:pk>', contactos_delete, name = 'borrar'),
]