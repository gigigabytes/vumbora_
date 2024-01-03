from .forms import UsuarioForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login 
from .models import Usuario
from .forms import EventoCadastro
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Evento


class CadastrarPerfilService:
    def cadastrar_perfil(self, request):
        form = UsuarioForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            usuario = Usuario.objects.create(
            user=user,
            nome=form.cleaned_data['nome'],
            tipo=form.cleaned_data['tipo'],
            identidade=form.cleaned_data['identidade'],
            foto=form.cleaned_data['foto'],
            email = form.cleaned_data['email']
        )
            
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return True
        else:
            return False
        
class LogarService:
    def Logar(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                messages.success(request,f'Hi {user.get_username()}, welcome back!')
                return True
            else:
                messages.error(request,f'Invalid username or password') 
                return False

class CadastrarEventoService:
    def cadastrar_evento(self, request):
        form = EventoCadastro(request.POST, request.FILES)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.usuario = request.user.usuario 
            evento.save()
            form.save_m2m()

            messages.success(request, 'Evento cadastrado com sucesso.')
            return True
        else:
            messages.error(request, 'Erro ao cadastrar evento. Verifique os campos.')
            return False
