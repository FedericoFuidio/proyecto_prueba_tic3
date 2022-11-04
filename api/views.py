from email.policy import default
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from .serializars import CompradorSerializer, LikeSerializer, DislikeSerializer, UserSerializer, VehiculoSerializer, VendedorSerializer
from .model.user import User
from .model.comprador import Comprador
from .model.vendedor import Vendedor
from .model.vehiculo import Vehiculo
from .model.like import Like
from .model.dislike import Dislike
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
            return JsonResponse({'result':'invalid', 'user':'el usuario no existe'})
        if('mail' in keys and 'password' in keys):
            user = User.objects.filter(mail = json_request['mail'])  # filtro por mail
        elif('id' in keys):
            user = User.objects.filter(id = json_request['id']) # filtro por id
        else:
            return JsonResponse({'result':'invalid', 'user':'el usuario no existe'})
        serializer = UserSerializer(user, many=True)
        try:
            data = json.loads(json.dumps(serializer.data))[0] # Primer (y unico) usuario devuelto
        except:
            return JsonResponse({'result':'invalid', 'user':'el usuario no existe'})
        password = data['password']
        
        if(password.__eq__(json_request['password'])): # chequeo de contraseña
            # Devolvemos username o password indistintamente. Lo necesario para poder buscar 
            # Al usuario en la base de datos luego de iniciar la sesion
            return JsonResponse({"result":"valid", "user":data['id']})
        return JsonResponse({"result":"invalid", 'user':'contraseña incorrecta'})

    # def post(self, request, **args):
    #     json_request = request_to_json(request)
    #     try:
    #         keys = json_request.keys()
    #     except:
    #         return JsonResponse({'result':'invalid', 'user':'request error'})
    #     if('mail' in keys and 'password' in keys and 'first_name' in keys and 'last_name' in keys):
    #         serializer = UserSerializer(data = request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         return JsonResponse({'result':'invalid', 'user':'no existe el usuariots'})
        


class VendedorView(generics.CreateAPIView):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

    #Cambiar request data por params (request.get)
    def get(self, request):
        json_request = request_to_json(request)
        try:
            keys = json_request.keys()
        except:
            return JsonResponse({'result':'invalid request'})

        if('id' in keys):
            vendedor = Vendedor.objects.filter(user = json_request['id']) # Filtra por el id
            # id = request.data.get('id', default = None)
        else:
            return JsonResponse({'result':'invalid request'})
        
        serializer = VendedorSerializer(vendedor, many=True)
        data = json.loads(json.dumps(serializer.data)) # Primer (y unico) usuario devuelto

        if(len(data) == 0):
            return JsonResponse({'result':'false'})
        else:
            return JsonResponse({'result':'true'})
        


        # try:
        #     if(vendedor[0]['id_id'] != None): # Si la busqueda devuelve un resultado sin errores
        #         return JsonResponse({'result':'true'})
        #     return JsonResponse({'result':'false'})
        # except:
        #     return JsonResponse({'result':'false'})


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

        json_request = request_to_json(request) #Parametros en el metodo get
        try:
            keys = json_request.keys()

        except:
            return JsonResponse({'result':'invalid'})            

        if('vendedor' in keys): #filtro por vendedor
            item = Vehiculo.objects.filter(vendedor = json_request['vendedor'])
        else:
            # Por defecto devolvemos todos los vehiculos:
            item = Vehiculo.objects.filter()

        serializer = VehiculoSerializer(item, many=True)
        data = json.loads(json.dumps(serializer.data))
        try:
            data = json.loads(json.dumps(serializer.data))
        except:
            return JsonResponse({'result':'error'})

        p=0
        for i in data:
            p=+1
            try:
                # Encode image with base64
                with open(i['imagen'][1:], "rb") as image_file:
                    image_data = base64.b64encode(image_file.read()).decode('utf-8')
                    
                i['imagen'] = image_data
                    
            except:
                JsonResponse({'result':'error', 'data':'error imagenes'})
                
        if p==0:
            return JsonResponse({'result':'error', 'data':'no hay'})
        return JsonResponse({'result':'ok', 'data':data})
        
        
class LikeView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    
    def get(self, request):
        json_request = request_to_json(request) #Parametros en el metodo get
        try:
            keys = json_request.keys()
        except:
            return JsonResponse({'result':'invalid'})

        if(not ('comprador' in keys) and not ('vehiculo' in keys)):
            return JsonResponse({'result':'invalid keys'})
        elif('comprador' in keys and not ('vehiculo' in keys)):
            item = Like.objects.filter(comprador = json_request['comprador'])  # filtro por id comprador
            if('info_completa' in keys):
                serializer = LikeSerializer(item, many = True)
                data = json.loads(json.dumps(serializer.data))
                for i in data: #Recorremos todos los vehiculos:
                    vehiculo = Vehiculo.objects.filter(id = i["vehiculo"])
                    serializer_vehiculo = VehiculoSerializer(vehiculo, many = True)
                    data_vehiculo = json.loads(json.dumps(serializer_vehiculo.data))
                    with open(data_vehiculo[0]['imagen'][1:], "rb") as image_file:
                        image_data = base64.b64encode(image_file.read()).decode('utf-8')

                    data_vehiculo[0]["imagen"] = image_data
                    i["data_vehiculo"] = data_vehiculo[0] # Sobreescribo vehiculo, se usa en initView

                    user = User.objects.filter(id = data_vehiculo[0]["vendedor"])
                    serializer_user= UserSerializer(user, many = True)
                    data_user = json.loads(json.dumps(serializer_user.data))
                    i["data_vendedor"] = data_user[0]
                    # Buscamos tambien los datos del vendedor del vehiculo
                return JsonResponse({'result':'ok', 'data': data})
                
        elif(not ('comprador' in keys) and 'vehiculo' in keys):
            item = Like.objects.filter(vehiculo = json_request['vehiculo'])  # filtro por id vehiculo
        elif('comprador' in keys and 'vehiculo' in keys):
            item = Like.objects.filter(comprador = json_request['comprador'], vehiculo = json_request['vehiculo'])  # filtro por vehiculo y comprador
        


        serializer = LikeSerializer(item, many=True)
        try:
            data = json.loads(json.dumps(serializer.data))
            return JsonResponse({'result':'ok', 'data': data})
        except:
            # json.loads dara una excepcion si no existe el like.
            return JsonResponse({'result':'invalid'})

    def delete(self, request):
        json_request = request_to_json(request)
        try:
            keys = json_request.keys()
        except:
            return JsonResponse({'result':'invalid'})

        if('comprador' in keys and 'vehiculo' in keys):
            item = Like.objects.get(comprador = json_request['comprador'], vehiculo = json_request['vehiculo'])  # filtro por vehiculo y comprador
            if item is not None:
                item.delete()
                return JsonResponse({'result':'ok'})
            else:
                return JsonResponse({'result':'like not exists'})
        else:
            return JsonResponse({'result':'invalid'})



    
    # POST like: Recibe like y comprador


class DislikeView(generics.CreateAPIView):
    queryset = Dislike.objects.all()
    serializer_class = DislikeSerializer

    def get(self, request):
        json_request = request_to_json(request) #Parametros en el metodo get
        try:
            keys = json_request.keys()
        except:
            return JsonResponse({'result':'invalid'})

        if(not ('comprador' in keys) and not ('vehiculo' in keys)):
            return JsonResponse({'result':'invalid keys'})
        elif('comprador' in keys and not ('vehiculo' in keys)):
            item = Dislike.objects.filter(comprador = json_request['comprador'])  # filtro por id comprador
        elif(not ('comprador' in keys) and 'vehiculo' in keys):
            item = Dislike.objects.filter(vehiculo = json_request['vehiculo'])  # filtro por id vehiculo
        elif('comprador' in keys and 'vehiculo' in keys):
            item = Dislike.objects.filter(comprador = json_request['comprador'], vehiculo = json_request['vehiculo'])  # filtro por vehiculo y comprador
        
        serializer = DislikeSerializer(item, many=True)
        try:
            data = json.loads(json.dumps(serializer.data))
            return JsonResponse({'result':'ok', 'data': data})
        except:
            # json.loads dara una excepcion si no existe el like.
            return JsonResponse({'result':'invalid'})

    def delete(self, request):
        json_request = request_to_json(request)
        try:
            keys = json_request.keys()
        except:
            return JsonResponse({'result':'invalid'})
            
        if('comprador' in keys and 'vehiculo' in keys):
            item = Dislike.objects.get(comprador = json_request['comprador'], vehiculo = json_request['vehiculo'])  # filtro por vehiculo y comprador
            if item is not None:
                item.delete()
                return JsonResponse({'result':'ok'})
            else:
                return JsonResponse({'result':'dislike not exists'})
        else:
            return JsonResponse({'result':'invalid'})



