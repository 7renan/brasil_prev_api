from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
import pytz

# models
from .models import ContratacaoPlano
from apps.customers.models import Cliente
from apps.products.models import Produto

# services
from brasil_prev_api.services import validate_date_contract, validate_max_age, validate_minimal_age, validate_value_aport,\
    validate_initial_care


# serializers
from .serializers import ContratacaoPlanoSerializer, ContratacaoPlanoSerializerResponseSave

utc = pytz.utc


class ContratacaoPlanoView(viewsets.ModelViewSet):
    serializer_class = ContratacaoPlanoSerializer
    queryset = ContratacaoPlano.objects.all()

    def create(self, request, *args, **kwargs):
        id_client = request.data.get('idCliente', False)
        id_product = request.data.get('idProduto', False)
        aport = request.data.get('aporte', False)
        # convert datestring in date
        contract_date = datetime.strptime(
            request.data['dataDaContratacao'], "%Y-%m-%d")
        customer = get_object_or_404(Cliente, pk=id_client)
        product = get_object_or_404(Produto, pk=id_product)

        last_contract = ContratacaoPlano.objects.filter(idCliente=customer.pk)

        # validations
        validate_date_contract(product.expiracaoDeVenda, contract_date)
        validate_max_age(customer.dataDeNascimento)
        validate_minimal_age(customer.dataDeNascimento)
        validate_value_aport(aport, product.getValorMinimoAporteInicial())
        if not last_contract.exists():
            validate_initial_care(
                contract_date, product.carenciaInicialDeResgate)

        # create contract plan
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            contract = serializer.save()
            contract_serialized = ContratacaoPlanoSerializerResponseSave(
                {'id': contract.pk})
            return Response(contract_serialized.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
