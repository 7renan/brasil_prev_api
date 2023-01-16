from django.db import models

# models
from apps.products.models import Produto
from apps.customers.models import Cliente


class ContratacaoPlano(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idProduto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    aporte = models.FloatField()
    dataDaContratacao = models.DateTimeField()



