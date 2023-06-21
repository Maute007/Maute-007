from django.contrib import admin
from .models import *

admin.site.register(Category)

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'category', 'data')
admin.site.register(Noticia, NoticiaAdmin)


class ComentariosAdmin(admin.ModelAdmin):
    list_display = ("noticia", "nome", "email", "telefone", "comentario", "status")
    readonly_fields = ("noticia", "nome", "email", "telefone", "comentario", )
admin.site.register(Comentarios, ComentariosAdmin)

#contador (countdown)
admin.site.register(Timer)

#efeito de digitacao
admin.site.register(Tiped)
