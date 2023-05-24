from django.db import models
from django.utils.html import format_html

class Candidatos(models.Model):
    
    STATUS = (
        ('Pendentes', 'Pendentes'),
        ('Visualizadas', 'Visualizadas')
    )
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=190)
    exp = models.TextField(max_length=900)
    skills =models.TextField(max_length=900)
    file = models.FileField()
    criado = models.d

