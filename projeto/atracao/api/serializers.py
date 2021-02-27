from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from atracao.models import Atracao


class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('id', 'nome', 'descricao', 'periodo')
