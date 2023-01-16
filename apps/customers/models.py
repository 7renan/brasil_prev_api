from django.db import models


class Cliente(models.Model):

    class Sexos(models.TextChoices):
        M = 'M', 'Masculino'
        F = 'F', 'Feminino'

    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=150)
    email = models.CharField(max_length=50)
    dataDeNascimento = models.DateTimeField()
    sexo = models.CharField(max_length=10, choices=Sexos.choices)
    rendaMensal = models.IntegerField()

    def __str__(self):
        return self.nome

    def getRendaMensal(self):
        return self.rendaMensal/100
