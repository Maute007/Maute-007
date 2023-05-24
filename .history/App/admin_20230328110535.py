from django.contrib import admin
from App.models import Candidatos

class CandidatosAdmin(admin.ModelAdmin):
    readonly_fields = ('id', ' name', 'phone', 'email', 'exp', 'skills', 'file') #("__all__")
    list_display = 12
