# Arquivo: restaurante/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from APP import views

# 👇 1. IMPORTAR A FERRAMENTA DE PADRÕES I18N
from django.conf.urls.i18n import i18n_patterns

# ----------------------------------------------------------------
# URLs que NÃO precisam de tradução (admin, login, etc.)
# ----------------------------------------------------------------
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='APP/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='criar_reserva'), name='logout'),
    
    # 👇 2. ADICIONAR A URL "FERRAMENTA" QUE OS BOTÕES VÃO USAR
    # Ela deve ficar FORA dos patterns
    path('i18n/', include('django.conf.urls.i18n')),
]

# ----------------------------------------------------------------
# URLs que SERÃO traduzidas (o seu site principal)
# ----------------------------------------------------------------
urlpatterns += i18n_patterns(
    # 👇 3. SUAS URLS DO APP FICAM AQUI DENTRO
    path('', views.criar_reserva, name='home'),
    path('', include('APP.urls')),
    
    # O Django agora vai criar as URLs:
    # /pt-br/
    # /en/
    # /es/
)


