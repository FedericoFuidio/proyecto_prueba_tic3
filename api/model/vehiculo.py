from unittest.util import _MAX_LENGTH
from django.db import models
from .vendedor import Vendedor

class Vehiculo(models.Model):
    tipo_publicacion = models.TextChoices('Alquiler', 'Venta')
    modelo = models.CharField(max_length=100, default="")
    tipo = models.CharField(blank=True, choices=tipo_publicacion.choices, max_length=10)
    marca = models.CharField(max_length=100, default="")
    matricula = models.CharField(max_length=100, default="", unique=True)
    precio_base = models.IntegerField()
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)