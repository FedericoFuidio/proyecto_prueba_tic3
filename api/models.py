from unittest.util import _MAX_LENGTH
from django.db import models
import string
import random
from django.core.validators import RegexValidator
from django.forms import PasswordInput
from .model.user import User

# Modelo de base de datos aca:
# Create your models here.

# Genera un numero aleatoreo para pasarle a code
def generate_unique_code():
    lenght = 8
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k = lenght))
        # Verificamos que el codigo no esta usado:
        if Room.objects.filter(code=code).count() == 0:
            break

    return code


class Room(models.Model):
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    address = models.TextField(default="")

    # Podemos crear funciones en el modelo

class Person(models.Model):
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    address = models.TextField(default="")

# Vlidar Mail, pedir telefono






