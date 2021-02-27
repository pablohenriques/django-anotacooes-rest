from rest_framework.viewsets import ModelViewSet
from comentario.models import Comentario
from .serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer