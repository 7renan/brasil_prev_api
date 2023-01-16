from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    susep = models.CharField(max_length=20)
    expiracaoDeVenda = models.DateTimeField()
    valorMinimoAporteInicial = models.IntegerField()
    valorMinimoAporteExtra = models.IntegerField()
    idadeDeEntrada = models.IntegerField()
    idadeDeSaida = models.IntegerField()
    carenciaInicialDeResgate = models.IntegerField()
    carenciaEntreResgates = models.IntegerField()

    def __str__(self):
        return self.nome

    def getValorMinimoAporteInicial(self):
        return self.valorMinimoAporteInicial/100

    def getValorMinimoAporteExtra(self):
        return self.valorMinimoAporteExtra/100
