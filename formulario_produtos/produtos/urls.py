from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_produtos, name='listar_produtos'),
    path('cadastro/', cadastrar_produto, name='cadastrar_produto'),
    path('visualizar/<str:id>/', visualizar_produto, name='visualizar_produto'),
    path('deletar/<str:id>/', deletar_produto, name='deletar_produto'),
    path('alterar/<str:id>/', alterar_produto, name='alterar_produto'),
    path('exportar/', exportar_excel, name='exportar_excel'),
]