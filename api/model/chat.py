from unittest.util import _MAX_LENGTH
from django.db import models
from .like import Like

class Chat(models.Model):
    like = models.OneToOneField(Like, on_delete=models.CASCADE)
    calif_vendedor = models.IntegerField()
    calif_comprador = models.IntegerField()