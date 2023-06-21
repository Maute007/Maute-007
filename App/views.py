from django.shortcuts import render
from .models import *
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import Noticia, Timer
#from datetime import datetime
from .forms import ComentariosForm


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
       
    noticias_destaque = Noticia.objects.order_by('-data')[:4]
    noticias_passadas = Noticia.objects.order_by('-data')[4:] 

    # Processar categorias destacadas para exibir apenas uma vez
    categorias_destaque = []
    categorias_processadas = set()
    for noticia in noticias_destaque:
        if noticia.category not in categorias_processadas:
            categorias_destaque.append(noticia.category)
            categorias_processadas.add(noticia.category)

    context = {
        'noticias_destaque': noticias_destaque,
        'categorias_destaque': categorias_destaque,
        'noticias_passadas': noticias_passadas,
        'categorias_processadas': categorias_processadas,
        
    }
    return render(request, 'home.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def novas(request):
    #timer = Timer.objects.all()
    #tiped = Tiped.objects.all()
    
    all_news = Noticia.objects.all()
    context = {
        'all_news': all_news,
        
        #'timer': timer,
        #'tiped':tiped,
    }
    return render(request, 'novas.html',context)

# Detalhe
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def detalhe(request, id):
    #data_atualizar = datetime.now().strftime("%H:%M:%S")
    noticia = Noticia.objects.get(pk=id)
    related = Noticia.objects.filter(category=noticia.category).exclude(pk=id) if noticia.category else []
    context = {
        'noticia': noticia,
        #'data_atualizar': data_atualizar,
        'related': related
    }
    return render(request, 'detalhe.html', context)


#Contacto formulario
#send email Maute
def MSG(request):
    if request.method == "POST":
        form = ComentariosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Envio bem sucedido.")
            return HttpResponseRedirect('/novas')
    else:
        form = ComentariosForm()
        return render(request, 'novas.html', {'form': form})
    return HttpResponseRedirect('novas')


