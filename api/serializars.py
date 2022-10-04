from dataclasses import field
from rest_framework import serializers
from .models import Room, Person, User, Vendedor

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

        # Deprecated:
        #field = ('id', 'code', 'host', 'guest_can_pause',
         #            'votes_to_skip', 'created_at')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'

        