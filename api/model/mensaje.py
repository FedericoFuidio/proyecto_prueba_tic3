from unittest.util import _MAX_LENGTH
from django.db import models
from .chat import Chat

class Mensaje(models.Model):
    emisor = models.TextChoices('Comprador', 'Vendedor')
    # chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    fechahora = models.DateTimeField(choices = emisor.choices, max_length = 10)
    contenido = models.CharField(blank = False, max_length = 100)
    enviado_por = models.CharField(blank = False, )