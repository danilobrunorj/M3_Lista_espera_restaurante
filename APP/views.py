# APP/views.py

# 1. Imports organizados em um só lugar
from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
# ... (seus outros imports)

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

from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva # Importe seu modelo de Reserva
@login_required
# Sua view existente
def gerenciar_reservas(request):
    
    # 1. BUSCAR OS DADOS DO BANCO
    # (Substitua 'Reserva' pelo nome real do seu modelo, se for diferente)
    lista_de_reservas = Reserva.objects.all().order_by('-data_reserva') # Pega todas as reservas
    contagem_confirmadas = Reserva.objects.filter(confirmada=True).count() # Conta as confirmadas

    # 2. CRIAR O DICIONÁRIO 'context'
    # Este é o passo que estava faltando.
    context = {
        'reservas': lista_de_reservas,
        'reservas_confirmadas_count': contagem_confirmadas,
    }

    # 3. ENVIAR O 'context' PARA O TEMPLATE
    # Agora a variável 'context' existe e o erro vai desaparecer.
    return render(request, 'APP/gerenciar_reservas.html', context)
# 👇 ADICIONE ESTAS DUAS NOVAS FUNÇÕES 👇

def editar_reserva(request, reserva_id):
    
    # 1. Busca a reserva exata que o usuário clicou para editar
    reserva = get_object_or_404(Reserva, id=reserva_id)

    if request.method == 'POST':
        # 2. Se o usuário está SALVANDO as mudanças (enviou o formulário)
        #    Preenchemos o formulário com os dados novos (request.POST)
        #    e dizemos qual 'instance' (objeto) estamos editando.
        form = ReservaForm(request.POST, instance=reserva)
        
        if form.is_valid():
            form.save() # Salva as mudanças no banco
            return redirect('gerenciar_reservas') # Volta para a lista
    
    else:
        # 3. Se o usuário acabou de CLICAR no botão "Editar" (método GET)
        #    Apenas criamos o formulário, pré-preenchido com os dados
        #    da 'instance' (reserva) que encontramos.
        form = ReservaForm(instance=reserva)

    # 4. Prepara o 'context' para enviar ao template
    context = {
        'form': form
        # Você pode adicionar a reserva se quiser, ex: 'reserva': reserva
    }
    
    # 5. Renderiza a página de formulário (A MESMA da criação)
    #    mas agora o 'form' no context virá preenchido.
    return render(request, 'APP/formulario_reserva.html', context)


def excluir_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    
    # Adicione lógica para excluir, por exemplo:
    # if request.method == 'POST': # É uma boa prática usar POST para excluir
    #     reserva.delete()
    #     return redirect('gerenciar_reservas')
    
    # Por enquanto, vamos apenas excluir e redirecionar:
    reserva.delete()
    print(f"DEBUG: Excluindo reserva ID: {reserva_id}")
    return redirect('gerenciar_reservas') # Redireciona de volta para a lista


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


# No topo do seu arquivo views.py, certifique-se de que os imports estão corretos
from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm  # <-- É MUITO IMPORTANTE importar seu formulário

# ... (suas outras views) ...

#
# SUBSTITUA SUA FUNÇÃO ANTIGA POR ESTA
#
# No topo do seu arquivo views.py, certifique-se de que os imports estão corretos
from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm  # <-- Garanta que seu formulário está sendo importado

# ... (suas outras views) ...

def editar_reserva(request, id):
    # 1. Busca a reserva correta pelo ID ou retorna um erro 404
    reserva = get_object_or_404(Reserva, id=id)

    # 2. Se o formulário foi enviado (método POST)
    if request.method == 'POST':
        # Cria uma instância do formulário com os dados enviados (request.POST)
        # e a instância da reserva que estamos editando (instance=reserva)
        form = ReservaForm(request.POST, instance=reserva)
        
        # 3. Valida o formulário
        if form.is_valid():
            form.save()  # Salva as alterações no banco de dados
            
            # Redireciona para o NOME DA URL da lista de reservas
            return redirect('gerenciar_reservas') 
            
    # 4. Se o método for GET (primeiro acesso à página)
    else:
        # Cria uma instância do formulário já preenchida com os dados da reserva
        form = ReservaForm(instance=reserva)

    # A LINHA FINAL QUE ESTAVA FALTANDO:
    # 5. Renderiza a página do formulário, passando o formulário como contexto.
    # Esta linha é executada em requisições GET ou se o formulário POST for inválido.
    return render(request, 'APP/formulario_reserva.html', {'form': form})

    # CORREÇÃO 2: Renderiza o template do formulário, passando o formulário como contexto
    # O caminho do template foi corrigido para 'APP/...'
    return render(request, 'APP/formulario_reserva.html', {'form': form})

    # Se for o primeiro acesso (GET), apenas mostra o formulário preenchido
    # Você pode reutilizar o mesmo template do formulário de 'adicionar reserva'
    return render(request, 'seu_app/formulario_reserva.html', {'reserva': reserva})

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

def criar_admin_temporario(request):
    try:
        # Tenta criar o superusuário
        # ATENÇÃO: Troque a senha 'admin' por uma senha mais forte se quiser
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        return HttpResponse("Usuário 'admin' criado com sucesso! <br><b>Delete esta URL e view imediatamente.</b>")
    except Exception as e:
        # Caso o usuário 'admin' já exista
        return HttpResponse(f"Erro ao criar usuário (ele já pode existir): {e}")
