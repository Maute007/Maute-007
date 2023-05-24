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
    criado = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS)
    
    #Control Read / Unread messages on admin.py
    def situation(self):
        if self.STATUS =='Visualizadas':
            return format_html('<span style="color: green">{0}</span>', self.status)
        else:
            return format_html('<span style="color: red">{0}</span>', self.status)
    situation.allow_tags = True
    
    def __str__(self):
        return self.n


