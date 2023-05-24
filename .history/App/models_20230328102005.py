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
    phone,
    address
    exp,
    skills


