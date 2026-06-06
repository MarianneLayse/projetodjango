from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from core.models import Estado, Municipio, Bairro

# Create your models here.
class PontoTuristico(models.Model):

    CATEGORIAS= [
        ('praia','Praia'),
        ('museu','Museu'),
        ('parque','Parque'),
        ('igreja','Igreja'),
        ('monumento','Monumento'),
        ('rio','Rio'),
        ('outro','Outro'),
    ]

    nome        = models.CharField(max_length=150)
    descricao   = models.TextField()
    categoria   = models.CharField(max_length=20, choices=CATEGORIAS)
    estado      = models.ForeignKey(Estado, on_delete=models.DO_NOTHING)
    municipio   = ChainedForeignKey(
        Municipio,
        chained_field='estado',
        chained_model_field='estado',
        show_all= False,
        sort= True,
        on_delete=models.DO_NOTHING
        )

    bairro      = ChainedForeignKey(
        Bairro, 
        chained_field='municipio',
        chained_model_field='municipio',
        show_all= False,
        sort= True,
        on_delete=models.DO_NOTHING
        )
    logradouro  = models.CharField(max_length=150)
    numero      = models.CharField(max_length=10)
    complemento = models.CharField(max_length=150, null=True, blank=True)
    cep         = models.CharField(max_length=9)
    ativo       = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    latitude    = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude   = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)


    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    ponto = models.ForeignKey(PontoTuristico, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    nota = models.IntegerField()
    comentario = models.TextField()
