from django.db.models import fields
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from pontosturisticos.models import PontoTuristico
from atracao.api.serializers import AtracaoSerializer
from endereco.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    enderecos = EnderecoSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'aprovacao', 'foto',
            'atracoes', 'enderecos', 'descricao_completa',
            'descricao_completa2'
        )

    def get_descricao_completa(self, obj):
        return f'{obj.nome} {obj.descricao}'