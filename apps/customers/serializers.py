from rest_framework import serializers

from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'email', 'dataDeNascimento', 'sexo', 'rendaMensal']


class ClienteSerializerResponseSave(serializers.Serializer):
    id = serializers.CharField()
