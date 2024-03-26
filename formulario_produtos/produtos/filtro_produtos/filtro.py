from django.db.models import Q
from ..models import Produto

def validar_campos_filtro(request):
    nome = request.GET.get('nome')

    filtro = Q()
    if nome:
        filtro &= Q(nome__contains=nome)

    produtos = Produto.objects.filter(filtro)
    return produtos