from django.contrib import admin
from .models import PontoTuristico
# Register your models here.

@admin.register(PontoTuristico)
class PontoTuristicoAdmin(admin.ModelAdmin):
    list_display = ('nome','categoria','estado','municipio','bairro','ativo')
    list_filter  = ('categoria','estado','municipio','ativo')
    search_fields= ('nome','descricao','logradouro')