from django.db import models


#send email
class Send(models.Model):
    email = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
    class Meta:
        verbose_name_plural = "Inscritos"
        
#CountDown )contagem regreciva
class Timer(models.Model):
    id =models.IntegerField(primary_key=True)
    timer = models.CharField(max_length=100, blank=True)
    
    class Meta:
        verbose_name_plural = "Contagem regressiva" 
        
# efeito de digitacao
class Tiped(models.Model):
    id =models.IntegerField(primary_key=True)
    fixo = models.CharField(max_length=50)
    txt01 = models.CharField(max_length=50)
    txt02 = models.CharField(max_length=50)
    txt03 = models.CharField(max_length=50)
    txt04 = models.CharField(max_length=50)
    
    def __str__(self):
        return self.fixo
    class Meta:
        verbose_name_plural = "Efeito de digitação" 
         
# MUSIC
class Music(models.Model):
    id = models.IntegerField(primary_key=True)
    title_music = models.CharField(max_length=100, null=False)  
    music = models.FileField()

    def __str__(self):
        return self.title_music

    class Meta:
        verbose_name_plural = "Musica do fundo"

#Slide de imagens
class Images(models.Model):
    titulo = models.CharField(max_length=50)
    img_01 = models.CharField(max_length=50, blank=True)
    img_02 = models.CharField(max_length=50, blank=True)
    img_03 = models.CharField(max_length=50, blank=True)
    img_04 = models.CharField(max_length=50, blank=True)
    img_05 = models.CharField(max_length=50, blank=True)
    img_06 = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Slides de Imagem'
    
# Imagem Padrao no Slide
class Padrao(models.Model):
    titulo = models.CharField(max_length=50)
    img_padrao = models.CharField(max_length=50, blank=True)
   
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Imagem Padrao'

#Homepage( formulario principal )
class Home(models.Model):
    id = models.IntegerField(primary_key=True)
    #titlo
    home_title = models.CharField(max_length=50)
    icon_title = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)
    #card 1(green)
    card_title01 = models.CharField(max_length=50)
    card_color01 = models.CharField(max_length=50)
    card_icon01 = models.CharField(max_length=50)
    txt_card_a1 = models.CharField(max_length=50)
    txt_card_b1= models.CharField(max_length=50)
    txt_card_c1= models.CharField(max_length=50)
    #card 2(red)
    card_title02 = models.CharField(max_length=50)
    card_color02 = models.CharField(max_length=50)
    card_icon02 = models.CharField(max_length=50)
    txt_card_a2 = models.CharField(max_length=50)
    txt_card_b2= models.CharField(max_length=50)
    txt_card_c2= models.CharField(max_length=50)
    #info (icon de perguntas)
    btn_color= models.CharField(max_length=50)
    icon_type = models.CharField(max_length=50)
    #Modal popup
    Modal_title = models.CharField(max_length=50)
    Modal_card_title = models.CharField(max_length=50)
    modal_card_color =  models.CharField(max_length=50)
    modal_card_icon = models.CharField(max_length=50)
    cargo01 = models.CharField(max_length=50)
    cargo02 = models.CharField(max_length=50)
    cargo03 = models.CharField(max_length=50)
    cargo04 = models.CharField(max_length=50)
    cargo05 = models.CharField(max_length=50)
    def __str__(self):
        return self.home_title
    
    class Meta:
        verbose_name_plural = "Pagina Principal"
    