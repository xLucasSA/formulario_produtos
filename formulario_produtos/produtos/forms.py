from django import forms
from .models import Produto    

class FormularioProduto(forms.ModelForm): 
    class Meta:
        model = Produto
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'valor': 'Valor (R$)',
            'descricao': 'Descrição',
            'disponivel': 'Disponível para Venda?'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for campo in self.fields:
            self.fields[campo].widget.attrs['class'] = 'form-control'

            if campo == 'valor':
                self.fields[campo].widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'R$', 'step': '0.01'})


class FiltroProduto(forms.ModelForm):
    
    class Meta:
        model = Produto
        fields = ['nome', 'disponivel']
        labels = {
            'nome': 'Nome',
            'disponivel': 'Disponibilidade'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for campo in self.fields:
            self.fields[campo].widget.attrs['class'] = 'form-control'
            self.fields[campo].widget.attrs['placeholder'] = campo
            self.fields[campo].widget.attrs['name'] = campo
            self.fields[campo].required = False
