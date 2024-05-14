from django.shortcuts import render
from rest_framework import viewsets, renderers, permissions
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Mensagens, Users, Imagem
from .serializers import *
from PIL import Image
import os
import time
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


class AcessarUsuario(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    objectSelf = Users.objects
    objectAmigos = Amigos.objects
    serializer_class = GenericClassUserSerializer

    def list(self, request, nome, sessionId=None):
        userValidation = self.objectSelf.filter(nome=nome).first() != None
        if(not userValidation):
            if(sessionId == None):
                return Response({'status' : False, 'msg' : 'É preciso de um sessionId para logar com um usuário novo!'})
            self.objectSelf.create(nome=nome, sessionId=sessionId)
        elif(sessionId != None):
            user = self.objectSelf.filter(nome=nome).first()
            user.sessionId = sessionId
            user.save()
        user = self.objectSelf.filter(nome=nome).first()
        serializer = GenericClassUserSerializer(user)
        return Response({'status' : True, 'data' : serializer.data})

class CriarAmizade(viewsets.ModelViewSet):
    queryset = Amigos.objects.all()
    objectSelf = Amigos.objects
    objectUser = Users.objects
    serializer_class = GenericClassUserSerializer

    def list(self, request, nome, amigo):
        userValidationExiste = self.objectUser.filter(nome=nome).first() != None
        if(not userValidationExiste):
            return Response({'status' : False, 'msg' : 'Seu usuário é invalido!'})
        amigoValidationExiste = self.objectUser.filter(nome=amigo).first() != None
        if(not amigoValidationExiste):
            return Response({'status' : False, 'msg' : 'Amigo não existe!'})
        validation = len(self.objectSelf.filter(nome__in=[nome, amigo]))
        amigoValidationExisteAmbos = validation == 2
        if(not amigoValidationExisteAmbos):
            idUser = self.objectUser.filter(nome=nome).first().id
            self.objectSelf.create(nome=amigo, idUser=idUser)
            idAmigo = self.objectUser.filter(nome=amigo).first().id
            self.objectSelf.create(nome=nome, idUser=idAmigo)
            return Response({'status' : True, 'msg' : 'Amizade criada!'})
        else:
            return Response({'status' : False, 'msg' : 'Amizade já existe!'})

class SalvarImagem(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = GenericClassImageSerializer

@csrf_exempt
def uploadImage(request):
    if request.method == 'POST':
        files = request.FILES
        filesLength = len(list(request.FILES.dict()))
        link = []
        for i in range(filesLength):
            timeAtual = round(time.time())
            img = Image.open(files.get(str(i + 1)))
            imgName = f'{timeAtual}_{i + 1}.{img.format.lower()}'
            path = os.path.join(settings.BASE_DIR, f'media/{imgName}')
            img = img.save(path)
            link.append(f'http://gustakx.pythonanywhere.com/media/{imgName}')
        return JsonResponse({'status' : True, 'msg' : link})

# class MensagemViewSet(viewsets.ModelViewSet):
#     queryset = Mensagens.objects.all()
#     serializer_class = MensagemSerializer

#     def list(self, request):
#         queryset = Mensagens.objects.all()
#         serializer = MensagemSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         return redirect('/mensagem/' + pk)

# class vazio(viewsets.ModelViewSet):
#     queryset = Mensagens.objects.all()
#     serializer_class = MensagemSerializer

#     def list(self, request):
#         return Response({})

#     def retrieve(self, request, pk=None):
#         return Response({})

# class MensagemViewSetOnlyRead(viewsets.ModelViewSet):
#     queryset = Mensagens.objects.all()
#     serializer_class = MensagemSerializerOnlyRead

#     def retrieve(self, request, pk=None):
#         queryset = Mensagens.objects.filter(id=pk).first()
#         serializer = MensagemSerializerOnlyRead(queryset)
#         if(serializer.data['Dmsg'] == 'Mensagem não encontrada!'):
#             return Response({'msg' : 'Usuário não encontrado'})
#         return Response(serializer.data)

#     def list(self, request):
#         return redirect('/mensagens/')

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = Users.objects.all()
#     serializer_class = UserSerializer

#     def list(self, request):
#         queryset = Users.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         return redirect('/user/' + pk)

# class UserViewSetOnlyRead(viewsets.ModelViewSet):
#     queryset = Users.objects.all()
#     serializer_class = UserSerializerOnlyRead

#     def retrieve(self, request, pk=None):
#         queryset = Users.objects.filter(id=pk).first()
#         serializer = UserSerializerOnlyRead(queryset)
#         if(serializer.data['nome'] == ''):
#             return Response({'msg' : 'Usuário não encontrado!'})
#         return Response(serializer.data)

#     def list(self, request):
#         return redirect('/users/')

# class AmigoViewSet(viewsets.ModelViewSet):
#     queryset = Amigos.objects.all()
#     serializer_class = AmigoSerializer

#     def list(self, request):
#         queryset = Amigos.objects.all()
#         serializer = AmigoSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         return redirect('/amigo/' + pk)

# class AmigoViewSetOnlyRead(viewsets.ModelViewSet):
#     queryset = Amigos.objects.all()
#     serializer_class = AmigoSerializerOnlyRead

#     def retrieve(self, request, pk=None):
#         queryset = Amigos.objects.filter(id=pk).first()
#         serializer = AmigoSerializerOnlyRead(queryset)
#         if(serializer.data['nome'] == ''):
#             return Response({'msg' : 'Amigo não encontrado!'})
#         return Response(serializer.data)

#     def list(self, request):
#         return redirect('/amigos/')