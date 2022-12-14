from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import RegexValidator

class User(models.Model):
    id = models.BigAutoField(primary_key = True)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    mail = models.EmailField(max_length=100, unique=True)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 16, null = True, default = "")
    password = models.CharField(max_length=100, default="")

