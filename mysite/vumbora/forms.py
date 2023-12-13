from django import forms

from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota', 'comentario', 'usuario'] # campos que serão exibidos no formulário
        widgets = {
            'comentario': forms.Textarea(attrs={'class': 'form-comentario', 'placeholder': 'Comentário', 'id': 'id_comentario'}),
        }