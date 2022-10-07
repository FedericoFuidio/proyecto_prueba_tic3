from unittest.util import _MAX_LENGTH
from django.db import models
from .vehiculo import Vehiculo
from .vendedor import Vendedor

class Dislike(models.Model):
    comprador = models.ForeignKey(Vendedor, on_delete=models.CASCADE, primary_key=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, primary_key=True)
    fechahora = models.DateTimeField()