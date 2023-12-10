from django.shortcuts import render, redirect
from .models import Evento, Usuario,Avaliacao
from .forms import AvaliacaoForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse


# Create your views here.
def index (request):
    evento_list = Evento.objects.order_by('datahora')[:5]
    context = {
        'evento_list': evento_list
    }
    return render(request,'vumbora/index.html',context)

def details (request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    return render(request,'vumbora/detail.html',{'evento':evento})


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
            return JsonResponse({'success': True})
            return HttpResponseRedirect(reverse('vumbora:avaliacao', args=(evento.id,)))
        else:
            return render(request, 'vumbora/avaliacao.html', {'evento': evento, 'avaliacoes': avaliacoes, 'form': form})