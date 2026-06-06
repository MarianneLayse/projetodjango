from django.db import models
# Create your models here.
class Estado(models.Model):

    REGIOES=[
        ('N','Norte'),
        ('NE','Nordeste'),
        ('CO','Centro-oeste'),
        ('SE','Sudeste'),
        ('S','Sul'),
    ]

    nome= models.CharField(max_length=100)
    sigla= models.CharField (max_length=2)
    regiao= models.CharField(max_length=25, choices=REGIOES, null=True, blank=True)

    def __str__(self):
        return f'{self.nome} - {self.sigla}'

class Municipio(models.Model):
    nome= models.CharField(max_length=100)
    populacao= models.IntegerField()
    estado= models.ForeignKey(
        Estado,
        on_delete=models.DO_NOTHING
    )

    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'
        ordering = ['nome','populacao']

    def __str__(self):
        return f'{self.nome} - {self.estado.sigla}'

class Bairro(models.Model):
    nome= models.CharField(max_length=100)
    populacao= models.IntegerField()
    municipio= models.ForeignKey(
        Municipio,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.nome