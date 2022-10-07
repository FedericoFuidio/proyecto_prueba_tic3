from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from .serializars import UserSerializer, VendedorSerializer
from .models import Room, Person
from .model.user import User
from .model.comprador import Comprador
from .model.vendedor import Vendedor
from .model.vehiculo import Vehiculo
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from django.contrib.auth import get_user
import json


# Create your views here.
def request_to_json(request):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        return None

    return data

def api_home(request, *args, **kwargs):
    # request -> HttpRequest
    body = request.body
    print("URL query parameters:")
    print(request.GET) # URL query parameters
    print(body)
    data = {} # diccionario vacio
    try:
        # Json.loads toma una string de JSON y la transforma en un diccionario
        data = json.loads(body)
        
    except:
        pass
    print(data)

    return JsonResponse({"Message":"Respuesta del backend"})

    # json data: request.body

def main(request):
    return HttpResponse("<h1> Hello")

# Luego de generar la vista debemos linkearla a un a url, en urls.py a nivel de api
# Cambiando 'generics.CreateAPIView' por 'generics.ListApiView' muestra una lista de toda la tabla 

class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Retorna el usuario con el last_name enviado
    # Falta hacer que retorne ante cualquier combinacion de parametros pasados
    def get(self, request, **args):
        json_request = request_to_json(request)
        try:
            keys = json_request.keys()
        except:
            return Response(status=status.HTTP_200_OK)
        if('last_name' in keys):
            user = User.objects.filter(last_name = json_request['last_name'])
        else:
            user = User.objects.filter()
        serializer = UserSerializer(user, many=True)
        print("Datos")
        data = json.dumps(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VendedorView(generics.CreateAPIView):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer