from django.shortcuts import render
from .models import Evento
from django import forms


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

def pesquisar_eventos(request):
    if request.method == 'GET':
        form = forms.Form(request.GET)
        if form.is_valid():
            termo_pesquisa = form.cleaned_data['termo_pesquisa']
            eventos = Evento.objects.filter(nome__icontains=termo_pesquisa)
        else:
            eventos = Evento.objects.all()
    else:
        form = forms.Form()
        eventos = Evento.objects.all()

    return render(request, 'resultado_pesquisa.html', {'form': form, 'eventos': eventos})