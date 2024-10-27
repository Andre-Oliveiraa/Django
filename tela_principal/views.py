from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'tela_principal/index.html')