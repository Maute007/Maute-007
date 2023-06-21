from django import forms
from .models import Comentarios

#Contact
class ComentariosForm(forms.ModelForm):
    class Meta: 
        model = Comentarios
        fields = "__all__"