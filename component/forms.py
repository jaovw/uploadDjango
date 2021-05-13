from django import forms
from .models import Produto,Pedido


class pedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('Nome', 'Quantidade','Descrição')





        
