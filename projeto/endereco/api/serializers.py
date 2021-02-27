from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from endereco.models import Endereco


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'endereco', 'cidade', 'estado')