from django.contrib import admin
from . models import Evento, Usuario, Local, Avaliacao

# Register your models here.
admin.site.register(Evento)
admin.site.register(Usuario)
admin.site.register(Local)
admin.site.register(Avaliacao)

