# APP/views.py

# 1. Imports organizados em um só lugar
from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm

# 2. View para criar a reserva
def criar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reserva_sucesso')
    else:
        form = ReservaForm()

    contexto = {'form': form}
    return render(request, 'APP/formulario_reserva.html', contexto)

# 3. View para a página de sucesso
def reserva_sucesso(request):
    # CORREÇÃO: Adicionado o caminho 'APP/' aqui também
    return render(request, 'APP/reserva_sucesso.html')

# 4. View para gerenciar as reservas
# APP/views.py

def gerenciar_reservas(request):
    # Pega todas as reservas
    lista_de_reservas = Reserva.objects.all().order_by('-data_reserva', '-criado_em')
    
    # Calcula o total de reservas confirmadas
    reservas_confirmadas = lista_de_reservas.filter(confirmada=True).count()
    
    contexto = {
        # A chave DEVE ser 'reservas', como no original
        'reservas': lista_de_reservas,
        # Adicionamos a contagem para o template usar
        'reservas_confirmadas_count': reservas_confirmadas
    }
    
    return render(request, 'APP/gerenciar_reservas.html', contexto)

# 5. View para excluir uma reserva
def excluir_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    
    if request.method == 'POST':
        reserva.delete()
        return redirect('gerenciar_reservas')
    
    # Se o método não for POST, apenas redireciona de volta
    return redirect('gerenciar_reservas')
# APP/views.py

def cardapio(request):
    return render(request, 'APP/cardapio.html')