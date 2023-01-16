from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response

# serializers
from .serializers import AporteExtraSerializer, AporteExtraResponseSave, ResgateSerializer, \
    ResgateSerializerResponseSave

# models
from .models import AporteExtra, Resgate
from apps.customers.models import Cliente
from apps.products.models import Produto
from apps.plans.models import ContratacaoPlano

# services
from brasil_prev_api.services import validate_minimal_value_aport_extra, validate_initial_care, validate_value_rescue


class AporteExtraView(viewsets.ModelViewSet):
    serializer_class = AporteExtraSerializer
    queryset = AporteExtra.objects.all()

    def create(self, request, *args, **kwargs):
        customer = get_object_or_404(Cliente, pk=request.data['idCliente'])
        plan = get_object_or_404(ContratacaoPlano, pk=request.data['idPlano'])
        aport_value = request.data.get('valorAporte', False)
        if aport_value:
            validate_minimal_value_aport_extra(int(aport_value), plan.aporte)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            aport_extra = serializer.save()
            aport_extra_serialized = AporteExtraResponseSave({'id': aport_extra.pk})
            return Response(aport_extra_serialized.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResgateView(viewsets.ModelViewSet):
    serializer_class = ResgateSerializer
    queryset = Resgate.objects.all()

    def create(self, request, *args, **kwargs):
        plan = get_object_or_404(ContratacaoPlano, pk=request.data['idPlano'])
        product_plan = get_object_or_404(Produto, id=plan.idProduto.pk)
        rescue_value = request.data.get('valorResgate', False)
        # validations
        if rescue_value:
            validate_value_rescue(plan.aporte, int(rescue_value))
            validate_initial_care(plan.dataDaContratacao, product_plan.carenciaInicialDeResgate)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            rescue = serializer.save()
            rescue_serialized = ResgateSerializerResponseSave({'id': rescue.pk})
            return Response(rescue_serialized.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
