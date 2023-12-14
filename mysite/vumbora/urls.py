from django.urls import path
from . import views

app_name = 'vumbora'
urlpatterns = [
    path('', views.index, name='index'),
    path('evento/<int:evento_id>/', views.details, name='details'),
    path('avaliacao/<int:evento_id>', views.avaliacao, name='avaliacao'),
    path('lista_eventos_semana/', views.eventos_na_semana, name='lista_eventos_semana'),
]