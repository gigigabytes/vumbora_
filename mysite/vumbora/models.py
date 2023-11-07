from django.db import models
from django.utils.timezone import now

# Create your models here.
class Usuario(models.Model):
    usuario_nome = models.CharField(max_length=200, default='SOME STRING')
    usuario_email = models.EmailField(max_length=200, default='SOME STRING')
    usuario_tipo = models.CharField(max_length=14,default = 'F' ,choices=[
        ('F', 'Física'),
        ('J', 'Jurídica')
    ])
    

class Local(models.Model):
    local_nome = models.CharField(max_length=200, default= 'Nome')
    local_bairro = models.CharField(max_length=200)
    local_cep = models.CharField(max_length=8, default ='Inserir')
    local_rua= models.CharField(max_length=200, default ='Inserir')
    local_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    local_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    local_estacionamento = models.BooleanField(default =True)

class Evento(models.Model):
    evento_nome = models.CharField(max_length=200)
    evento_datahora = models.DateTimeField(default = now)
    evento_genero = models.CharField(max_length=200)
    evento_valor = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    # evento_local = models.ForeignKey(Local, on_delete=models.CASCADE)

