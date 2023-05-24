from django import forms
from App.models import Candidatos

class CandidatosForm(forms.ModelForm):
    file = forms.FileField(required=True)
    class Meta