from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    tipo = models.CharField(max_length=1,default = 'F' ,choices=[
        ('F', 'Física'),
        ('J', 'Jurídica')
    ])
    identidade = models.CharField(max_length =14)
    foto = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return self.nome

class Bairro(models.Model):
    nome = models.CharField(max_length= 200)
    zona = models.CharField(max_length=2, choices=[
        ('ZN', 'Zona Norte'),
        ('ZS','Zona Sul'),
        ('ZL', 'Zona Leste'),
        ('ZO', 'Zona Oeste')
    ])
    def __str__(self):
        return self.nome

class Local(models.Model):
    verbose_name = "Locais" 
    nome = models.CharField(max_length=200)
    bairro = models.ForeignKey(Bairro,on_delete=models.CASCADE, null=True)
    cep = models.CharField(max_length=20)
    rua= models.CharField(max_length=200)
    numero = models.CharField(max_length=4, blank = True)
    estacionamento = models.BooleanField(default = True)
    class Meta:
        verbose_name_plural = "Locais"
    def __str__(self):
        return self.nome


class Genero(models.Model):
    genero = models.CharField(max_length=1,choices =[
        ('E', 'Exposição'),
        ('F', 'Festa'),
        ('G', 'Gastronomia'),
        ('S', 'Show'),
        ('T','Teatro'),  
    ])
    class Meta:
        verbose_name_plural = "Gêneros"
    def __str__(self):
        choices_dict = {
            'E': 'Exposição',
            'F': 'Festa',
            'G': 'Gastronomia',
            'S': 'Show',
            'T': 'Teatro',     
        }
        return choices_dict.get(self.genero, '')
    
class Evento(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200, null=True)
    datahora = models.DateTimeField(default = now)
    valor = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, null=True)
    arte = models.ImageField(upload_to='images/', null=True, blank = True)
    genero = models.ManyToManyField(Genero)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    nota = models.IntegerField(default=5,blank= True,validators=[MaxValueValidator(5), MinValueValidator(1)])
    comentario = models.CharField(max_length=200, null=True,blank=True)
    data = models.DateTimeField(default = now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE, null=True)    

class Comenta(models.Model):
    comentario = models.CharField(max_length=200)
    data_hora = models.DateTimeField(default=now)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE,null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True)
    class Meta:
        verbose_name_plural = "Comentários"

class Images(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="evento_images", null = True)
    class Meta:
        verbose_name_plural = "Images"
# python -m pip install Pill
