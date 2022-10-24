
from email.policy import default
from django.db import models
from .user import User

class Comprador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)