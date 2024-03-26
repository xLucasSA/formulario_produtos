from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_produtos, name='listar_produtos'),
    path('cadastro/', cadastrar_produto, name='cadastrar_produto'),
    path('visualizar/<str:id>', cadastrar_produto, name='visualizar_produto'),
    path('exportar/', exportar_excel, name='exportar_excel'),
]
