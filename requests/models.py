from django.db import models
import time
import os

def directory_path(instance, filename):
    arquivo, extensao = os.path.splitext(filename)
    return "{0}{1}".format(round(time.time()), extensao)

class Mensagens(models.Model):
    DtoFrom = models.CharField(max_length=50)
    Dto = models.CharField(max_length=50)
    Dfrom = models.CharField(max_length=50)
    Dmsg = models.TextField()
    DidCriacao = models.IntegerField()

    def __str__ (self):
        return self.DtoFrom

class Users(models.Model):
    nome = models.CharField(max_length=50)
    sessionId = models.CharField(max_length=20)

    def __str__ (self):
        return self.nome
    
    def details(self):
        return {'nome' : self.nome, 'sessionId' : self.sessionId}

class Amigos(models.Model):
    nome = models.CharField(max_length=50)
    idUser = models.IntegerField()

    def __str__ (self):
        return self.nome

class Imagem(models.Model):
    nome = models.CharField(max_length=255)
    imagem = models.FileField(upload_to=directory_path, blank=True)

    def __str__ (self):
        return self.nome