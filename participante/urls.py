from django.conf.urls import url

from . import views
app_name = "participantes"

urlpatterns = [
    url('^lista-participantes-partidas-lol/$', views.lista_participantes_partidas_lol, name='lista-participantes-partidas-LOL'),
    url('^lista-participantes-partidas-fifa/$', views.lista_participantes_partidas_fifa, name='lista-participantes-partidas-FIFA'),
    url('^lista-participantes-partidas-cs/$', views.lista_participantes_partidas_cs, name='lista-participantes-partidas-CSGO'),
    url('^novo-participante/$', views.novo_participante, name='novo-participante'),
    url('^editar-participante/(?P<id>[0-9]+)/$', views.editar_participante, name='editar-participante'),
    url('^excluir-participante/(?P<id>[0-9]+)/$', views.excluir_participante, name='excluir-participante'),
    url('^nova-partida/$', views.nova_partida, name='nova-partida'),
    url('^editar-partida/(?P<id>[0-9]+)/$', views.editar_partida, name='editar-partida'),
    url('^excluir-partida/(?P<id>[0-9]+)/$', views.excluir_partida, name='excluir-partida'),
]