# APP/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.criar_reserva, name='criar_reserva'),
    path('sucesso/', views.reserva_sucesso, name='reserva_sucesso'),
    path('gerenciar/', views.gerenciar_reservas, name='gerenciar_reservas'),
    path('excluir/<int:reserva_id>/', views.excluir_reserva, name='excluir_reserva'),
    path('cardapio/', views.cardapio, name='cardapio'),
    
    # URL de edição
    path('reserva/editar/<int:id>/', views.editar_reserva, name='editar_reserva'),
    
]