from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# serializers
from .serializers import ClienteSerializer
from .models import Cliente
from .serializers import ClienteSerializer, ClienteSerializerResponseSave


class ClienteView(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            customer_serialized = ClienteSerializerResponseSave(data={'id': customer.pk})
            if customer_serialized.is_valid():
                return Response(customer_serialized.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
