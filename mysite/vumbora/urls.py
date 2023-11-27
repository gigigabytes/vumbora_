from django.urls import path
from . import views

app_name = 'vumbora'
urlpatterns = [
    path('', views.index, name='index'),
    path('vumbora/<int:evento_id>/', views.details, name='details'),
    path('vumbora/<int:evento_id>/avaliacao', views.avaliacao, name='avaliacao')
]