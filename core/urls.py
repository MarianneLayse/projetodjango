from django.urls import path
from . import views

urlpatterns = [
    path('estados/', views.listar_estados, name= 'listar_estados'),
    path('detalhes-estado/<int:id>/', views.detalhes_estado, name= 'detalhes_estado'),
    path ('cadastrar-estado', views.cadastrar_estado,name= 'cadastrar_estado'),
    path ('editar-estado/<int:id>/', views.editar_estado, name= 'editar_estado'),
    path ('apagar-estado/<int:id>/', views.apagar_estado, name= 'apagar_estado'),
    path('municipios/', views.listar_municipios, name= 'listar_municipios'),
    path('cadastrar-municipio', views.cadastrar_municipio, name= 'cadastrar_municipio'),
    path('detalhes-municipio/<int:id>/', views.detalhes_municipio, name= 'detalhes_municipio'),
    path('bairros/', views.listar_bairros, name= 'listar_bairros'),
    path('detalhes-bairro/<int:id>/', views.detalhes_bairro, name= 'detalhes_bairro'),

    path('municipios/por_estado/<int:estado_id>/', views.municipios_por_estado, name="municipios_por_estado"),
    path('bairros/por_municipio/<int:municipio_id>/', views.bairros_por_municipio, name="bairros_por_municipio"),
    path('pontos/por_municipio/<int:municipio_id>/', views.pontos_por_municipio, name="pontos_por_municipio"),
    path('pontos/json/<int:id>/', views.ponto_json, name="pontos_json"),
    
   

]
