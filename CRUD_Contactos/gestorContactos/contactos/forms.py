from django.forms import ModelForm
from .models import *

class ContactoModelForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'