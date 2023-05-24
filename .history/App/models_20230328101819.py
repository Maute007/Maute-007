from django.db import models
from django.utils.html import format_html

class Candidatos(models.Model):
    
    STATUS = (
        ('Pendentes', 'Pendentes'),
        ('Visualizadas', 'Visualizadas')
    )
    
    id = models.p

