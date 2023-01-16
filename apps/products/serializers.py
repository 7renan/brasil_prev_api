from rest_framework import serializers

# models
from .models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['nome', 'susep', 'expiracaoDeVenda', 'valorMinimoAporteInicial', 'valorMinimoAporteExtra',
                  'idadeDeEntrada', 'idadeDeSaida', 'carenciaInicialDeResgate', 'carenciaEntreResgates']


class ProdutoSerializerResponseSave(serializers.Serializer):
    id = serializers.CharField()
