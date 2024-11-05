from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.create_produto, name='home'),
    path('create_categoria/', views.create_categoria, name='categoria'),
    path('<int:pk>/editar/', views.editar_produto, name='editar'),
    path('<int:pk>/deletar/', views.deletar_produto, name='deleta'),
    path('<int:pk>/deletar_categoria/', views.deletar_categoria, name='deleta_categoria')
]