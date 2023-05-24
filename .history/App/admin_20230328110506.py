from django.contrib import admin
from App.models import Candidatos

class CandidatosAdmin(admin.ModelAdmin):
    readonly_fields = ('id', ' name', 'phone', 'email', 'exp', 'skills', '') #("__all__")

