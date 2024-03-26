from django import template

register = template.Library() 

@register.simple_tag
def calcular_indice(loop_atual, pagina, paginador):
    
    quantidade_anterior = int(pagina.number-1) * int(paginador.per_page)
    indice = quantidade_anterior + int(loop_atual)

    return indice