from django import forms
from django.shortcuts import render, redirect
from .models import Evento, Usuario,Avaliacao
from .forms import AvaliacaoForm
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

### View INDEX
############
def index (request):
    evento_list = Evento.objects.order_by('datahora')[:5]
    context = {
        'evento_list': evento_list
    }
    return render(request,'vumbora/index.html',context)


### View DETAIL
############
def details (request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    return render(request,'vumbora/detail.html',{'evento':evento})


class PesquisaEventoForm(forms.Form):
    termo_pesquisa = forms.CharField(label='Pesquisar Evento', max_length=100)

### View PESQUISAR Eventos
#############
def pesquisar_eventos(request):
    eventos = Evento.objects.all()

    if request.method == 'POST':
        form = PesquisaEventoForm(request.POST)
        if form.is_valid():
            termo_pesquisa = form.cleaned_data.get('termo_pesquisa', '')
            eventos = Evento.objects.filter(nome__icontains=termo_pesquisa)
    else:
        form = PesquisaEventoForm()

    return render(request, 'vumbora/resultado_pesquisa.html', {'form': form, 'eventos': eventos})

       
### View AVALIAÇÃO
##############
def avaliacao(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    avaliacoes = Avaliacao.objects.filter(evento_id=evento_id)

    if request.method == 'GET':
        form = AvaliacaoForm()
        return render(request, 'vumbora/avaliacao.html', {'evento': evento, 'avaliacoes': avaliacoes, 'form': form})
    elif request.method == 'POST':
        print(request.POST)
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            nova_avaliacao = form.save(commit=False)
            # avaliacao.usuario = request.user
            nova_avaliacao.evento = evento
            nova_avaliacao.save()
            # return JsonResponse({'success': True})
            return HttpResponseRedirect(reverse('vumbora:avaliacao', args=(evento.id,)))
        else:
            return render(request, 'vumbora/avaliacao.html', {'evento': evento, 'avaliacoes': avaliacoes, 'form': form})
            
### View EVENTOS na semana
##############
def eventos_na_semana(request):
     # Lógica para filtrar eventos da semana, se aplicável
    hoje = datetime.now()
    inicio_semana = hoje - timedelta(days=hoje.weekday())
    fim_semana = inicio_semana + timedelta(days=6)
    eventos_semana = Evento.objects.filter(datahora__range=[inicio_semana, fim_semana])

    # Adicione uma mensagem se não houver eventos
    mensagem_sem_eventos = "Não há eventos a serem realizados nesta semana." if not eventos_semana else None

    # Renderiza o template com os eventos
    return render(request, 'vumbora/lista_eventos_semana.html', {'eventos_semana': eventos_semana, 'mensagem_sem_eventos': mensagem_sem_eventos})
