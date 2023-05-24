from django.contrib import admin
from .models import Send, Timer, Tiped, Music, Home

#send email
class SendAdmin(admin.ModelAdmin):
    readonly_fields = ['email']
    list_display = ['email']
    search_fields = ['email']
    list_per_page = 10
admin.site.register(Send, SendAdmin)

# Countdown (Timer)
class CountdownAdmin(admin.ModelAdmin):
    list_display = ['timer'] 
    #nao permitir mais de um id
    def has_add_permission(self, *args, **kwargs):
        return not Timer.objects.exists()
admin.site.register(Timer, CountdownAdmin)

# efeito de digitacao
class TipedAdmin(admin.ModelAdmin):
    list_display = ['fixo'] 
    #nao permitir mais de um id
    def has_add_permission(self, *args, **kwargs):
        return not Tiped.objects.exists()
admin.site.register(Tiped, TipedAdmin)

#efeito de  Musica
class MusicAdmin(admin.ModelAdmin):
    list_display = ['title_music'] 
    #nao permitir mais de um id
    def has_add_permission(self, *args, **kwargs):
        return not Music.objects.exists()
admin.site.register(Music, MusicAdmin) 

#Homepage
class HomeAdmin(admin.ModelAdmin):
    list_display = ['home_title', ] 
    #nao permitir mais de um id
    def has_add_permission(self, *args, **kwargs):
        return not Home.objects.exists()
admin.site.register(Home, HomeAdmin) 
