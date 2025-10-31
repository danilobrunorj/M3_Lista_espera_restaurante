# APP/forms.py

from django import forms
from .models import Reserva
import re
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class ReservaForm(forms.ModelForm):

    def clean_data_reserva(self):
        data = self.cleaned_data.get('data_reserva')
        if data and data < timezone.now().date():
            # <--- CORREÇÃO 2: MENSAGEM DE ERRO PERSONALIZADA
            raise forms.ValidationError("Data anterior a atual, favor insira uma data válida.")
        return data

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        numeros = re.sub(r'\D', '', telefone)
        if len(numeros) != 11:
            raise forms.ValidationError("O telefone deve ter 11 dígitos (DDD + número).")
        return numeros

    class Meta:
        model = Reserva
        fields = ['nome_cliente', 'telefone', 'email', 'numero_de_pessoas', 'data_reserva', 'observacoes']
        labels = {
            'nome_cliente': _('Nome do Cliente'),
            'telefone': _('Telefone'),
            'email': _('E-mail'),
            'numero_pessoas': _('Número de Pessoas'),
            'data_reserva': _('Data da Reserva'),
            'observacoes': _('Observações'),
        }
        
        widgets = {
            # ... (outros widgets) ...
            'telefone': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'telefone-mask',
                'maxlength': '15', # Mantém o limite de 15 caracteres
                'placeholder': '(DD) XXXXX-XXXX' # <-- ADICIONE ESTA LINHA
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'telefone-mask',
                # <--- CORREÇÃO 1: LIMITA A DIGITAÇÃO NO CAMPO
                'maxlength': '15' 
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'seuemail@exemplo.com'
            }),
            'numero_de_pessoas': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'data_reserva': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date'
            }),
            'observacoes': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4
            }),
        }