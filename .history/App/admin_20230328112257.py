from django.contrib import admin
from .models import Candidatos

class CandidatosAdmin(admin.ModelAdmin):
    readonly_fields = ('id' ' name', 'age', 'email', 'phone', 'exp', 'skills', 'file') #("__all__")
    list_display = ['name', 'email', 'exp', 'skills', 'criado', 'situation']
    search_fields = ['name', 'email']
    list_filter = ['status']
    list_per_page = 12
    
admin.site.register(Candidatos, CandidatosAdmin)