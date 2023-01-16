from django.db import models

# models
from apps.customers.models import Cliente
from apps.plans.models import ContratacaoPlano


class AporteExtra(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idPlano = models.ForeignKey(ContratacaoPlano, on_delete=models.CASCADE)
    valorAporte = models.IntegerField()

    def getValorAporte(self):
        return self.valorAporte/100


class Resgate(models.Model):
    idPlano = models.ForeignKey(ContratacaoPlano, on_delete=models.CASCADE)
    valorResgate = models.IntegerField()

    def getValorResgate(self):
        return self.valorResgate/100
