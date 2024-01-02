from django import forms
from .models import Evento, Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    
class UsuarioForm(UserCreationForm):
    tipo = forms.ChoiceField(choices=[
        ('F', 'Física'),
        ('J', 'Jurídica')
    ])
    identidade = forms.CharField(max_length=14)
    foto = forms.ImageField(required=False)
    nome = forms.CharField(max_length=200)
    class Meta:
        model=User
        fields = ['username','email','password1','password2','nome', 'tipo', 'identidade', 'foto']

class EventoCadastro(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'descricao', 'datahora', 'valor', 'local', 'arte', 'genero']
        widgets = {
            'datahora': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        labels = {
            'datahora': 'Data e Hora do Evento',
        }