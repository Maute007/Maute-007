from django import forms
from .models import Candidatos

class CandidatosForm(forms.ModelForm):
    file = forms.FileField(required=True)
    class Meta:
        model = Candidatos
        fields = "__all__"