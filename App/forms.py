from django import forms
from .models import Send, Images

#send email
class SendEmail(forms.ModelForm):
    class Meta: 
        model = Send
        fields = "__all__"
        

class ImagesForm(forms.ModelForm):
    
    titulo = forms.CharField(
        min_length=3,
        max_length=50,
        widget=forms.TextInput(attrs={
            'style':'font-size: 13px',
            'placeholder':'De um titulo'
        })
    )
    
    img_01 = forms.FileField(
        label='',
        widget= forms.FileInput(attrs={
            'style':'font-size: 13px',
            'accept':'image/jpeg, image/jpeg',
            'class':'form-control-sm',
            }),
    )
    
    img_02 = forms.FileField(
        label='',
        widget= forms.FileInput(attrs={
            'style':'font-size: 13px',
            'accept':'image/jpeg, image/jpeg',
            'class':'form-control-sm',
            }),
    )
    
     
    img_03 = forms.FileField(
        label='',
        widget= forms.FileInput(attrs={
            'style':'font-size: 13px',
            'accept':'image/jpeg, image/jpeg',
            'class':'form-control-sm',
            }),
    )
    
    img_04 = forms.FileField(
        label='',
        widget= forms.FileInput(attrs={
            'style':'font-size: 13px',
            'accept':'image/jpeg, image/jpeg',
            'class':'form-control-sm',
            }),
    )
    
     
    img_05 = forms.FileField(
        label='',
        widget= forms.FileInput(attrs={
            'style':'font-size: 13px',
            'accept':'image/jpeg, image/jpeg',
            'class':'form-control-sm',
            }),
    )
    
    img_06 = forms.FileField(
        label='',
        widget= forms.FileInput(attrs={
            'style':'font-size: 13px',
            'accept':'image/jpeg, image/jpeg',
            'class':'form-control-sm',
            }),
    )
    
    class Meta:
        model = Images
        fields = '__all__'
    