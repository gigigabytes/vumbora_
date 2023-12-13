from django.shortcuts import render, get_object_or_404
from .models import Evento

# Create your views here.
def index (request):
    evento_list= Evento.objects.order_by('datahora')[:5]
    context = {
        'evento_list': evento_list
    }
    return render(request,'vumbora/index.html',context)

def details(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    context = {
        'evento': evento,
        'arte_url': evento.arte.url if evento.arte else None,
        'event' : Evento.objects.get(pk=evento.pk),
    }
    return render(request, 'vumbora/detail.html', context)