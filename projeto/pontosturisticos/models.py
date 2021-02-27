from django.db import models
from django.db.models.deletion import CASCADE
from atracao.models import Atracao
from comentario.models import Comentario
from avaliacao.models import Avaliacao
from endereco.models import Endereco


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=64)
    descricao = models.TextField()
    aprovacao = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    enderecos = models.ForeignKey(Endereco, on_delete=CASCADE)
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    @property
    def descricao_completa2(self):
        return f"{self.nome} - {self.descricao}"

    def __str__(self):
        return f"Nome: {self.nome} - Descricao: {self.descricao} - Aprovação: {self.aprovacao}"