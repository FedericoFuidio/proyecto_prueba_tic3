from dataclasses import field
from rest_framework import serializers

from .models import Room, Person
from .model.user import User
from .model.vehiculo import Vehiculo
from .model.comprador import Comprador
from .model.vendedor import Vendedor
from .model.like import Like
from .model.dislike import Dislike
from .model.chat import Chat


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'

class CompradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comprador
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
        