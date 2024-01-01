from django import forms
from .models import Evento 

class PesquisaEventoForm(forms.Form):
    termo_pesquisa = forms.CharField(label='Pesquisar Evento', max_length=100)
from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota', 'comentario', 'usuario'] # campos que serão exibidos no formulário
        widgets = {
            'comentario': forms.Textarea(attrs={'class': 'form-comentario', 'placeholder': 'Comentário', 'id': 'id_comentario'}),
        }

class EventoCadastro(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'descricao', 'datahora', 'valor', 'local', 'arte', 'genero',]
