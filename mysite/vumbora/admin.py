from django.contrib import admin
from . models import Evento, Usuario, Local, Bairro, Genero, Comenta

# Register your models here.
admin.site.register(Evento)
admin.site.register(Usuario)
admin.site.register(Local)
admin.site.register(Bairro)
admin.site.register(Comenta)
admin.site.register(Genero)