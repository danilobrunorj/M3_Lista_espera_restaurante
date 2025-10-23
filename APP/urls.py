# APP/urls.py
from django.urls import path  # <-- ESTA LINHA ESTAVA FALTANDO OU FOI APAGADA
from . import views

urlpatterns = [
    path('', views.criar_reserva, name='criar_reserva'),
    path('sucesso/', views.reserva_sucesso, name='reserva_sucesso'),
    path('gerenciar/', views.gerenciar_reservas, name='gerenciar_reservas'),
    path('excluir/<int:reserva_id>/', views.excluir_reserva, name='excluir_reserva'),
    path('cardapio/', views.cardapio, name='cardapio'),

    # Dê o nome 'editar_reserva' para a URL de edição
    

    path('reserva/editar/<int:id>/', views.editar_reserva, name='editar_reserva'),
    urlpatterns = [
    # ... (suas outras urls) ...

    # ADICIONE ESTA LINHA:
    path('criar-meu-admin-secreto-agora-12345/', views.criar_admin_temporario, name='criar_admin_temp'),
    ]

]