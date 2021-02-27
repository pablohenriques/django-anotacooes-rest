from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from pontosturisticos.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    #queryset = PontoTuristico.objects.filter(aprovacao=True)
    serializer_class = PontoTuristicoSerializer
    #permission_classes = (IsAuthenticated, )
    permission_classes = (DjangoModelPermissions, )
    authentication_classes = (TokenAuthentication, )
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao')
    lookup_field = 'nome'

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome=nome)
        if descricao:
            queryset = queryset.filter(descricao=descricao)

        return queryset

    #def list(self, request):
    #    return Response({'status-list': 'ok'})

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @action(methods=['GET'], detail=True)
    def nova_funcao(self, request, pk=None):
        return Response({'status-action': 'ok'})