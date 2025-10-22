# Versão CORRETA
from django.contrib import admin
from django.urls import path, include  # 1. Adicione 'include' aqui
from django.contrib.auth import views as auth_views

# Restaurante/urls.py
from APP import views

# Restaurante/urls.py
from django.contrib import admin
from django.urls import path, include
from APP import views  # Garanta que esta linha exista!

urlpatterns = [
    path('admin/', admin.site.urls),

    # Troque 'views.pagina_inicial' por 'views.criar_reserva'
    path('', views.criar_reserva, name='home'),
    
    # Inclua as outras URLs do seu APP para manter tudo funcionando
    path('', include('APP.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='APP/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='criar_reserva'), name='logout'), # 'criar_reserva' é o nome da sua home
]

