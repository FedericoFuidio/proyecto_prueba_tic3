from unittest.util import _MAX_LENGTH
from django.db import models
import string
import random
from django.core.validators import RegexValidator
from django.forms import PasswordInput

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
class User(models.Model):
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    mail = models.EmailField(max_length=100, default="", unique=True)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    password = models.CharField(max_length=100, default="")

class Vendedor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

class Comprador(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Vehiculo(models.Model):
    modelo = models.CharField(max_length=100, default="")
    marca = models.CharField(max_length=100, default="")
    matricula = models.CharField(max_length=100, default="", unique=True)
    precio_base = models.IntegerField()
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)




