from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path('edita/<int:pk>', views.edita_perfil, name='editar'),
]