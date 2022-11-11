from unittest.util import _MAX_LENGTH
from django.db import models
from .chat import Chat

class Mensaje(models.Model):
    emisor = models.TextChoices('enviado_por', 'comprador vendedor')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, null=False)
    fechahora = models.DateTimeField(auto_now_add = True)
    contenido = models.CharField(blank = False, max_length = 100)
    enviado_por = models.CharField(choices = emisor.choices, blank = False, max_length = 10)