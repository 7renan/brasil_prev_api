from rest_framework import serializers

# models
from .models import AporteExtra, Resgate


class ResgateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resgate
        fields = ['idPlano', 'valorResgate']


class ResgateSerializerResponseSave(serializers.Serializer):
    id = serializers.CharField()


class AporteExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = AporteExtra
        fields = ['idCliente', 'idPlano', 'valorAporte']


class AporteExtraResponseSave(serializers.Serializer):
    id = serializers.CharField()
