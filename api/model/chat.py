from unittest.util import _MAX_LENGTH
from django.db import models
from .like import Like

class Chat(models.Model):
    like = models.OneToOneField(Like, on_delete=models.CASCADE)
    fechahora = models.DateTimeField(auto_now_add = True)
    calif_vendedor = models.IntegerField(null=True)
    calif_comprador = models.IntegerField(null=True)