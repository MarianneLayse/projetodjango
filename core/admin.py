from django.contrib import admin
from .models import Estado, Municipio,Bairro
# Register your models here.
@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome','sigla','regiao')
    search_fields= ('nome','sigla')
    ordering = ('nome',)

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nome','estado','populacao')
    list_filter = ('estado',)
    search_fields= ('nome','estado__nome','estado__regiao')
    ordering = ('estado__nome','nome')

@admin.register(Bairro)
class BairroAdmin(admin.ModelAdmin):
    list_display = ('nome','municipio__nome', 'municipio__estado')
    list_filter = ('municipio', 'municipio__estado')
    search_fields= ('nome','municipio__nome','municipio__estado__nome')
    ordering = ('municipio__estado__nome','municipio__nome')

admin.site.site_header = 'Administração de Localidades'
admin.site.site_title = 'Sistema de Localidades'
admin.site.index_title = 'Painel Administrativo'