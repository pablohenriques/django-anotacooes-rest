from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from pontosturisticos.api.viewsets import PontoTuristicoViewSet
from atracao.api.viewsets import AtracaoViewSet
from endereco.api.viewsets import EnderecoViewSet
from avaliacao.api.viewsets import AvaliacaoViewSet
from comentario.api.viewsets import ComentarioViewSet

router = routers.DefaultRouter()
router.register('pontos_turisticos', PontoTuristicoViewSet, basename='PontoTuristico')
router.register('atracoes', AtracaoViewSet)
router.register('enderecos', EnderecoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)
router.register('comentarios', ComentarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
