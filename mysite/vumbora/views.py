from django.shortcuts import render
from .models import Evento
from django import forms

def index (request):
    evento_list= Evento.objects.order_by('datahora')[:5]
    context = {
        'evento_list': evento_list
    }
    return render(request,'vumbora/index.html',context)

def details (request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    return render(request,'vumbora/detail.html',{'evento':evento})

class PesquisaEventoForm(forms.Form):
    termo_pesquisa = forms.CharField(label='Pesquisar Evento', max_length=100)

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

       