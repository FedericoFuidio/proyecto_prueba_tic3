from dataclasses import field
from rest_framework import serializers
from .models import Room, Person
from .model.user import User
from .model.vehiculo import Vehiculo
from .model.comprador import Comprador
from .model.vendedor import Vendedor


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'

        