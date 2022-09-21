from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializars import PersonSerializer, RoomSerializer
from .models import Room, Person

# Create your views here.

def main(request):
    return HttpResponse("<h1> Hello")

# Vista general de un Room
# Luego de generar la vista debemos linkearla a un a url, en urls.py a nivel de api
# Cambiando 'generics.CreateAPIView' por 'generics.ListApiView' muestra una lista de toda la tabla 
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class PersonView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer