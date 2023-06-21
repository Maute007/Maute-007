from django.db import models

class Category(models.Model):
    titulo = models.CharField(max_length=150)
    img = models.ImageField(upload_to='img/')

    class Meta:
        verbose_name_plural = 'CATEGORIAS'

    def __str__(self):
        return self.titulo


class Noticia(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=500)
    img = models.ImageField(upload_to='img/')
    detalhes = models.TextField(max_length=1000, blank=True)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'NOTICIAS'

    def __str__(self):
        return self.titulo


class Comentarios(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=15)
    comentario = models.TextField(max_length=500, blank=True)
    status = models.BooleanField(default=False) 

    class Meta:
        verbose_name_plural = 'COMENTARIOS'

    def __str__(self):
        return "{} - {} - {}".format(self.comentario, self.nome, self.email)


class Timer(models.Model):
    timer = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = "CONTAGEM REGRESSIVA"


class Tiped(models.Model):
    fixo = models.CharField(max_length=50)
    txt01 = models.CharField(max_length=100)
    txt02 = models.CharField(max_length=100)
    txt03 = models.CharField(max_length=100)
    txt04 = models.CharField(max_length=100)

    def __str__(self):
        return self.fixo

    class Meta:
        verbose_name_plural = "EFEITO DE DIGITACAO"
