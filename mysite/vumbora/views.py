from django.shortcuts import render
from .models import Evento
from datetime import datetime, timedelta

# Create your views here.
def index (request):
    evento_list= Evento.objects.order_by('datahora')[:5]
    context = {
        'evento_list': evento_list
    }
    return render(request,'vumbora/index.html',context)

def details (request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    return render(request,'vumbora/detail.html',{'evento':evento})

def eventos_na_semana(request):
    # Obtém a data atual
    hoje = datetime.now()

    # Calcula o início e o fim da semana
    inicio_semana = hoje - timedelta(days=hoje.weekday())
    fim_semana = inicio_semana + timedelta(days=6)

    # Filtra os eventos da semana
    eventos_semana = Evento.objects.filter(data_inicio__range=[inicio_semana, fim_semana])

    # Renderiza o template com os eventos
    return render(request, 'seu_app/lista_eventos_semana.html', {'eventos_semana': eventos_semana})


