from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.login_user, name='main'),
    path('sair/', LogoutView.as_view(), name='sair'),
    path('cadastrar/', views.cadastrar_user, name='cadastrar')
]
