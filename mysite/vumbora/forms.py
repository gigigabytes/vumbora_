from django import forms

from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota', 'comentario', 'usuario']
        widgets = { 
            'comentario': forms.TextInput(attrs={'class': 'coment-text', 'placeholder': 'Comentário'})
           
            }