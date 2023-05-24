from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from App import views
from sms import settings

#Maute//Maute007
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('login', include('django.contrib.auth.urls'), name="login"),
    # enviar email
    path('send', views.send, name="send"),
    #=============********* backend ********==================
    path('central/', views.central, name="central"),
    #editar o countdown(contagem regressiva)
    path('editTime', views.editTime, name="editTime"),
    path('editTyped', views.editTyped, name="editTyped"),
    # URL para o vídeo estático
    path('song', views.song, name='song'),
    #Home page
    path('editHome', views.editHome, name='editHome'),
    
    path('slide/', views.slide, name='slide'),
    path('update/<int:id>', views.update, name='update'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
