from django.urls import path
from . import views

app_name = 'vumbora'
urlpatterns = [
    path('', views.index, name='index'),
    path('evento/<int:evento_id>/', views.details, name='details'),
    path('pesquisar_eventos/', views.pesquisar_eventos, name='pesquisar_eventos'),
    path('avaliacao/<int:evento_id>/', views.avaliacao, name='avaliacao'),
    path('lista_eventos_semana/', views.eventos_na_semana, name='lista_eventos_semana'),
    path('cadastrar_evento/', views.cadastrar_evento, name='cadastrar_evento'),
    path('logar/', views.logar, name='logar'),
    path('cadastrar_perfil/', views.cadastrar_perfil, name='cadastrar_perfil'),

]