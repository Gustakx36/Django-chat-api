from requests.views import *
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers, renderers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'imagem', SalvarImagem, basename='imagem')
# router.register(r'mensagem', MensagemViewSetOnlyRead, basename='mensagem/pk')
# router.register(r'users', UserViewSet, basename='user')
# router.register(r'user', UserViewSetOnlyRead, basename='user/pk')
# router.register(r'amigos', AmigoViewSet, basename='amigo')
# router.register(r'amigo', AmigoViewSetOnlyRead, basename='amigo/pk')
# router.register(r'conversaEmPartes', CriarAmizade, basename='conversaEmPartes')
# router.register(r'enviarMensagem', vazio, basename='enviarMensagem')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    re_path(r'^logarUser/(?P<nome>[a-zA-Z0-9]+)/?(?P<sessionId>[a-zA-Z0-9]+)?/?$', AcessarUsuario.as_view({'get' : 'list'})),
    re_path(r'^criarAmizade/(?P<nome>[a-zA-Z0-9]+)/?(?P<amigo>[a-zA-Z0-9]+)?/?$', CriarAmizade.as_view({'get' : 'list'})),
    re_path(r'^uploadImage/?$', uploadImage),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)