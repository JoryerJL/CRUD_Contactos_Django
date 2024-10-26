from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.IntegerField()
    email = models.EmailField()
