from django import forms
from App.models import Candidatos

class CandidatosForm(forms.ModelForm):
    file = f