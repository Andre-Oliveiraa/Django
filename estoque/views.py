from django.shortcuts import render
from sistema.models import *

# Create your views here.
def home_page(request):
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'estoque/index.html', {'produtos': produtos, 'categorias': categorias})