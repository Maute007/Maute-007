from django.contrib import admin
from App.models import Candidatos

class CandidatosAdmin(admin.ModelAdmin):
    readonly_fields = ('id', ' name', 'phone', 'email', 'exp', 'skills', 'file') #("__all__")
    list_display = ['name', 'email', 'exp', 'skills', 'criado', 'situation']
    search_fields = ['name', 'email']
    list_filter = ['status']
    list_per_page