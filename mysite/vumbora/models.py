from django.db import models
from django.utils.timezone import now

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    tipo = models.CharField(max_length=1,default = 'F' ,choices=[
        ('F', 'Física'),
        ('J', 'Jurídica')
    ])
    identidade = models.CharField(max_length =14)
    def __str__(self):
        return self.nome

class Local(models.Model):
    nome = models.CharField(max_length=200)
    bairro = models.CharField(max_length=1, choices=[
        ('R', 'Ribeira'),
        ('P', 'Ponta Negra'),
        ('T', 'Tirol'),
        ('I', 'Igapó'),
    ])
    cep = models.CharField(max_length=20)
    rua= models.CharField(max_length=200)
    numero = models.CharField(max_length=4, blank = True)
    estacionamento = models.BooleanField(default =True)
    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200, null=True)
    datahora = models.DateTimeField(default = now)
    genero = models.CharField(max_length=1,choices =[
        ('E', 'Exposição'),
        ('F', 'Festa'),
        ('G', 'Gastronomia'),
        ('S', 'Show'),
        ('T','Teatro'),  
    ])
    valor = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nome

