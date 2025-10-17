from django.contrib import admin
from .models import Reserva # Importa o modelo Reserva que você criou

# A classe que personaliza o admin
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'telefone', 'data_reserva', 'numero_de_pessoas', 'criado_em')
    search_fields = ('nome_cliente', 'email', 'telefone')
    list_filter = ('data_reserva', 'criado_em')
# APP/admin.py
