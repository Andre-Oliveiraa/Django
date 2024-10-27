from django.shortcuts import render, redirect
from .forms import Forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from sistema.models import *

# Create your views here.
def cadastrar_user(request):
    filiais = Filial.objects.all()  # Para exibir as opções de filial no template

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        filial_id = request.POST.get('filial') 
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')

        if username and email and password and filial_id and estado and cidade:
            filial = Filial.objects.get(id=filial_id)
            user = Gerente(
                username=username,
                email=email,
                filial=filial,
                estado=estado,
                cidade=cidade
            )
            user.set_password(password) 
            user.save() 
            login(request, user)
            return redirect('tela:home')
        else:
            print("Campos obrigatórios estão faltando.")

    return render(request, 'login/create.html', {'filiais': filiais})
    
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)    
                return redirect('tela:home')
    else:
        form = AuthenticationForm()
    return render(request, 'login/login.html', {'form': form, 'action': 'login'})
