from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from sistema.models import *

class Forms(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
    filial = forms.ModelChoiceField(queryset=Filial.objects.all(), required=True, label="Filial")

    class Meta:
        model = Gerente
        fields = ['username', 'email', 'filial', 'estado', 'cidade', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user