from django import forms
from .models import VendaSaida

class VendaSaidaForm(forms.ModelForm):
    class Meta:
        model = VendaSaida
        fields = ['descricao_produto', 'quantidade', 'valor_unitario', 'vendedor', 'observacoes']