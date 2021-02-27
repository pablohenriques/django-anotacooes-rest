from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from comentario.models import Comentario


class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('id', 'usuario', 'comentario', 'data')
        