from django.db import models


class Atracao(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    periodo = models.DateTimeField()

    def __str__(self):
        return f"Nome: {self.nome} - Descrição: {self.descricao} - Período: {self.periodo}"
  