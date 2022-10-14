from email.policy import default
from django.db import models
from .user import User

class Vendedor(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)