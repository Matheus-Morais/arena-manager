from django.conf.urls import url

from . import views
app_name = "participantes"

urlpatterns = [
    url('^lista-participantes-lol/$', views.lista_participantes_lol, name='lista-participantes-LOL'),
    url('^lista-participantes-fifa/$', views.lista_participantes_fifa, name='lista-participantes-FIFA'),
    url('^lista-participantes-cs/$', views.lista_participantes_cs, name='lista-participantes-CSGO'),
    url('^novo-participante/$', views.novo_participante, name='novo-participante'),
    url('^editar-participante/(?P<id>[0-9]+)/$', views.editar_participante, name='editar-participante'),
    url('^excluir-participante/(?P<id>[0-9]+)/$', views.excluir_participante, name='excluir-participante'),
]