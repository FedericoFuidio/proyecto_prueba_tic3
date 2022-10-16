from email.policy import default
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from .serializars import CompradorSerializer, LikeSerializer, UserSerializer, VehiculoSerializer, VendedorSerializer
from .models import Room, Person
from .model.user import User
from .model.comprador import Comprador
from .model.vendedor import Vendedor
from .model.vehiculo import Vehiculo
from .model.like import Like
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from django.contrib.auth import get_user
import json

import base64 #Transferencia de imagenes


# Create your views here.
def request_to_json(request):
    # body = request.body
    body = json.dumps(request.GET)
    data = {}
    try:
        data = json.loads(body)
    except:
        return None
    return data

def data_to_json(request):
    print(request.data)
    body = request.data
    data = {}
    try:
        data = json.loads(body)
    except:
        return None
    return data

def api_home(request, *args, **kwargs):
    # request -> HttpRequest
    body = request.body
    print(body)
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
 
# Hacer a mano el metodo POST para manejar las passwords y validar un mail
class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Hace consulta por mail
    # Busca en la base de datos por el mail pasado, y luego compara las passwords
    def get(self, request, **args):
        json_request = request_to_json(request) #Parametros en el metodo get
        try:
            keys = json_request.keys()
        except:
            return JsonResponse({'result':'invalid', 'user':'user not exist'})
        if('mail' in keys and 'password' in keys):
            user = User.objects.filter(mail = json_request['mail'])
        else:
            return JsonResponse({'result':'invalid', 'user':'user not exist'})
        serializer = UserSerializer(user, many=True)
        try:
            data = json.loads(json.dumps(serializer.data))[0] # Primer (y unico) usuario devuelto
        except:
            return JsonResponse({'result':'invalid', 'user':'user not exist'})
        password = data['password']
        
        if(password.__eq__(json_request['password'])):
            # Devolvemos username o password indistintamente. Lo necesario para poder buscar 
            # Al usuario en la base de datos luego de iniciar la sesion
            return JsonResponse({"result":"valid", "user":data['id']})
        return JsonResponse({"result":"invalid", 'user':'invalid password'})

class VendedorView(generics.CreateAPIView):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

    #Cambiar request data por params (request.get)
    def get(self, request):

        try:
            id = request.data.get('id', default = None)
            vendedor = Vendedor.objects.filter(id = id).values() # Filtra por el id pasado
        except:
            return JsonResponse({'result':'invalid request'})

        try:
            if(vendedor[0]['id_id'] != None): # Si la busqueda devuelve un resultado sin errores
                return JsonResponse({'result':'true'})
            return JsonResponse({'result':'false'})
        except:
            return JsonResponse({'result':'false'})


class CompradorView(generics.CreateAPIView):
    queryset = Comprador.objects.all()
    serializer_class = CompradorSerializer

    # Verificamos que un id es comprador:
    # Cambiar request data por request params (request.get)
    def get(self, request):

        try:
            id = request.data.get('id', default = None)
            comprador = Comprador.objects.filter(id = id).values() # Filtra por el id pasado
        except:
            return JsonResponse({'result':'invalid request'})

        try:
            if(comprador[0]['id_id'] != None): # Si la busqueda devuelve un resultado sin errores
                return JsonResponse({'result':'true'})
            return JsonResponse({'result':'false'})
        except:
            return JsonResponse({'result':'false'})

class VehiculoView(generics.CreateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

    #Usar parameters (request.get)
    def get(self, request):

        # En principio devolvemos todos los vehiculos:
        vehiculo = Vehiculo.objects.filter()
        serializer = VehiculoSerializer(vehiculo, many=True)
        data = json.loads(json.dumps(serializer.data))
        try:
            data = json.loads(json.dumps(serializer.data)) # Json de todos los vehiculos
        except:
            return JsonResponse({'result':'error'})

        for i in data:
            try:
                # Encode image with base64
                with open(i['image'][1:], "rb") as image_file:
                    image_data = base64.b64encode(image_file.read()).decode('utf-8')
                
                i['image'] = image_data
                
            except:
                JsonResponse({'result':'error', 'vehiculo':'error'})
            
        return JsonResponse({"result":"ok", "vehiculo":data})
        
class LikeView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    # POST like: Recibe like y comprador

