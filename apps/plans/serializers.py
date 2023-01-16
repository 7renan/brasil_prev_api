from rest_framework import serializers

# models
from .models import ContratacaoPlano


class ContratacaoPlanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContratacaoPlano
        fields = ['idCliente', 'idProduto', 'aporte', 'dataDaContratacao']


class ContratacaoPlanoSerializerResponseSave(serializers.Serializer):
    id = serializers.CharField()
