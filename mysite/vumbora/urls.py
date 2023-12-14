from django.urls import path
from . import views
from .views import pesquisar_eventos
#preciso colocar dessa forma? 

app_name = 'vumbora'
urlpatterns = [
    path('', views.index, name='index'),
    path('vumbora/<int:evento_id>/', views.details, name='details'),
    path('pesquisar_eventos/', views.pesquisar_eventos, name='pesquisar_eventos'),
    path('avaliacao/<int:evento_id>/', views.avaliacao, name='avaliacao')
]