from django.urls import path
from . import views

app_name = 'tela'

urlpatterns = [
    path('', views.home_page, name='home')
]