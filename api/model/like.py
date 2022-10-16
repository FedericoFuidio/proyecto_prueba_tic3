from datetime import datetime
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from .vehiculo import Vehiculo
from .comprador import Comprador

class Like(models.Model):
    # No es posible obtener el id del vehiculo, eventualmente se tendra que cambiar el modelo
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE, default="")
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, default="")
    fechahora = models.DateTimeField().auto_now_add

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['comprador', 'vehiculo'], name='unique_comprador_vehiculo_combination'
            )
        ]

