from django.shortcuts import get_object_or_404, render, redirect
from .forms import FormularioProduto, FiltroProduto
from .filtro_produtos.filtro import validar_campos_filtro
from .models import Produto
from django.core.paginator import Paginator
from openpyxl import Workbook
from django.http import HttpResponse

def listar_produtos(request):
    try:
        if request.GET:
            form = FiltroProduto(request.GET)
            produtos = validar_campos_filtro(request)

        else:
            form = FiltroProduto()
            produtos = Produto.objects.filter()
        
        paginator = Paginator(produtos, 10)

        numero_pagina = request.GET.get('page')
        pagina = paginator.get_page(numero_pagina)

                        
        for registro in pagina:
            registro.valor = 'R$ {:.2f}'.format(registro.valor).replace('.', ',')

        return render(request, 'listagem.html', context = {
            'pagina': pagina,
            'paginador': paginator,
            'form': form
        })
    except:
        return render(request, 'exeption.html')

def cadastrar_produto(request):
    try:
        if request.method == 'POST':
            form = FormularioProduto(request.POST)
            if form.is_valid():
                form.save()
                return redirect('listar_produtos')
        else:
            form = FormularioProduto()

        return render(request, 'cadastro.html', {'form': form})
    except:
        return render(request, 'exeption.html')

def exportar_excel(request):
    try:
        registros = validar_campos_filtro(request)

        wb = Workbook()
        ws = wb.active
        
        cabecalhos = [
            'Id',
            'Nome',
            'Descrição',
            'Valor'
        ]

        ws.append(cabecalhos)

        for registro in registros:
            linha = [
                registro.id,
                registro.nome,
                registro.descricao,
                registro.valor,
            ]
            ws.append(linha)
        
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=lista_produtos.xlsx'
        wb.save(response)

        return response
    except:
        return render(request, 'exeption.html')

def visualizar_produto(request, id):
    dados = get_object_or_404(Produto, pk=id)

    form = FormularioProduto(instance=dados)
    for campo in form.fields:
        form.fields[campo].widget.attrs['disabled'] = True
    
    return render(request, 'visualiza_produto.html', {'form': form, 'id': id})

def alterar_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)

    if request.method == 'POST':
        form = FormularioProduto(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = FormularioProduto(instance=produto)
    
    for campo in form.fields:
        form.fields[campo].widget.attrs['disabled'] = False

    return render(request, 'visualiza_produto.html', {'form': form, 'id': id})    

def deletar_produto(request, id):
    try:
        Produto.objects.filter(id=id).delete()

        return redirect('listar_produtos')
    except:
        return render(request, 'exeption.html')