from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Gerente)
admin.site.register(Filial)
admin.site.register(Produto)
admin.site.register(Estoque)
admin.site.register(RelatorioDeEstoque)
admin.site.register(Fornecedor)