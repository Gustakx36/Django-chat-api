from .models import Mensagens, Users, Amigos, Imagem
from rest_framework import serializers

class GenericClassUserSerializer(serializers.ModelSerializer):
    amigos = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = ['id', 'nome', 'sessionId', 'amigos']

    def get_amigos(self, obj):
        amigos = Amigos.objects.filter(idUser=obj.id)
        serializer = GenericClassAmigoSerializer(amigos, many=True)
        return serializer.data

class GenericClassAmigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amigos
        fields = ['id', 'nome', 'idUser']

class GenericClassImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = ['id', 'nome', 'imagem']

# class MensagemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Mensagens
#         fields = ['id', 'DtoFrom', 'Dto', 'Dmsg', 'Dfrom', 'DidCriacao']

# class MensagemSerializerOnlyRead(serializers.ModelSerializer):
#     class Meta:
#         model = Mensagens
#         fields = ['id', 'DtoFrom', 'Dto', 'Dfrom', 'Dmsg', 'DidCriacao']
#         read_only_fields = ['id', 'DtoFrom', 'Dto', 'Dfrom', 'DidCriacao']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = ['id', 'nome', 'sessionId']

# class UserSerializerOnlyRead(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = ['id', 'nome', 'sessionId']
#         read_only_fields = ['id']

# class AmigoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Amigos
#         fields = ['id', 'nome', 'idUser']

# class AmigoSerializerOnlyRead(serializers.ModelSerializer):
#     class Meta:
#         model = Amigos
#         fields = ['id', 'nome', 'idUser']
#         read_only_fields = ['id', 'idUser']