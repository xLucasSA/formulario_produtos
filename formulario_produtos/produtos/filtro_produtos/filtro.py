from django.db.models import Q
from ..models import Produto

def validar_campos_filtro(request):
    nome = request.GET.get('nome')
    disponivel = request.GET.get('disponivel')

    filtro = Q()

    if nome:
        filtro &= Q(nome__contains=nome)

    if disponivel:
        filtro &= Q(disponivel=disponivel)

    produtos = Produto.objects.filter(filtro)
    return produtos