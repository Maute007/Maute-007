from django.contrib import admin
from .models import *


class MeuAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'produto', 'entradas', 'saidas', 'quantidade', 'genero', 'contexto', 'Data_Criacao')
admin.site.register(Product, MeuAdmin)
