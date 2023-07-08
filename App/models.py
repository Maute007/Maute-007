from django.db import models
        
class Product(models.Model):
    
    #id = models.IntegerField(primary_key=True, auto_created=True)
    nome = models.CharField(max_length=80)
    telefone = models.IntegerField(max_length=15)
    produto = models.CharField(max_length=50)
    entradas = models.CharField(max_length=50)
    saidas = models.CharField(max_length=50)
    quantidade = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    contexto = models.TextField(max_length=100)
    status = models.CharField(max_length=40)
    Data_Criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.produto