from unittest.util import _MAX_LENGTH
from django.db import models
from .vehiculo import Vehiculo
from .comprador import Comprador

class Dislike(models.Model):
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE, null=False)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, null=False)
    fechahora = models.DateTimeField(auto_now_add = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['comprador', 'vehiculo'], name='dislike_unique_comprador_vehiculo_combination'
            )
        ]