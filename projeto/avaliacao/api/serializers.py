from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from avaliacao.models import Avaliacao


class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('id', 'user', 'comentario', 'nota', 'data')