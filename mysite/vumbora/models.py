from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario_nome: models.CharField(max_length=200);
    usuario_email: models.EmailField(max_length=254);
    usuario_tipo:models.CharField(max_length=14, choices=[
        ('F', 'Física'),
        ('J', 'Jurídica')
    ]);

class Evento(models.Model):
    evento_nome = models.CharField(max_length=200)
    evento_datahora = models.DateTimeField
    evento_genero = models.CharField(max_length=200)
    evento_valor = models.DecimalField

class Local(models.Model):
    local_estacionamento = models.BooleanField
    local_bairro = models.CharField(max_length=200)
    local_cep = models.CharField(max_length=8)
    local_rua=models.CharField(max_length=200)
    local_longitude = models.IntegerField
    local_latitude = models.IntegerField 
