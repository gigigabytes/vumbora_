from django.urls import path
from . import views

app_name = 'vumbora'
urlpatterns = [
    path('', views.index, name='index'),
    path('evento/<int:evento_id>/', views.details, name='details'),
    path('pesquisar_eventos/', views.pesquisar_eventos, name='pesquisar_eventos'),
    path('avaliacao/<int:evento_id>/', views.avaliacao, name='avaliacao'),
    path('lista_eventos_semana/', views.eventos_na_semana, name='lista_eventos_semana'),
    path('logar/', views.logar, name='logar'),
    path('cadastro_perfil/', views.cadastro_perfil, name='cadastro_perfil'),
]