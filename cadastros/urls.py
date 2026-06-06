from django.urls import path
from . import views


urlpatterns = [
    path('pontos-turisticos/', views.listar_pontos, name= 'listar_pontos'),
    path('pontos-turisticos/<int:id>/', views.detalhes_ponto, name='detalhes_ponto'),
    path('pontos-turisticos/<int:id>/editar/', views.editar_ponto, name='editar_ponto'),
    path('pontos-turisticos/<int:id>/excluir/', views.excluir_ponto, name='excluir_ponto'),
    path('pontos-turisticos/novo/', views.criar_ponto, name='criar_ponto'),
    path('pontos-turisticos/<int:id>/avaliar/', views.avaliar_ponto, name='avaliar_ponto'),
    path ("", views.index_pontos, name= 'index_pontos'),
]