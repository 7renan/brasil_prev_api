from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# serializers
from .serializers import ProdutoSerializer, ProdutoSerializerResponseSave

# models
from .models import Produto


class ProdutoView(viewsets.ModelViewSet):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            product_serialized = ProdutoSerializerResponseSave(data={'id': product.pk})
            if product_serialized.is_valid():
                return Response(product_serialized.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
