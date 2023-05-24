from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import Send, Timer, Tiped, Music, Home, Images, Padrao
from App.forms import SendEmail, ImagesForm
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse


#home page
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    timer = Timer.objects.all()
    tiped = Tiped.objects.all()
    music = Music.objects.all()
    home = Home.objects.all()
    padrao = Padrao.objects.all()
    context = {
        'timer': timer, 'tiped':tiped, 
        'music':music, 'home':home, 'padrao':padrao,
    }
    return render(request, 'index.html', context)

#send email Maute
def send(request):
    if request.method == "POST":
        form = SendEmail(request.POST)
        email = request.POST['email']
        if Send.objects.filter(email= email).exists():
            messages.error(request, "Esse email já está cadastrado!")
            return HttpResponseRedirect('/')
        elif form.is_valid():
            form.save()
            messages.success(request, "Envio bem sucedido.")
            return HttpResponseRedirect('/')
    else:
        form = SendEmail()
        return render(request, 'index.html', {'form': form})
    return HttpResponseRedirect('/') 

#==================Home (BACKEND)===========
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def central(request):
    #inscricoes
    Registro = Send.objects.all().order_by('-created')
    total = Send.objects.all().count()
    timer = Timer.objects.all()
    tiped = Tiped.objects.all()
    music = Music.objects.all()
    home = Home.objects.all()
    slide = Images.objects.all()
    context = {
        'Registro': Registro, 
        'total':total, 
        'timer':timer, 'tiped':tiped,
        'music':music, 'home':home,
        'slide':slide,
    }
    #--------------------------
    last_login = request.user.last_login
    now = datetime.now(last_login.tzinfo)
    # Forçar o usuário a fazer login novamente se já passou uma hora desde o último login
    if now - last_login > timedelta(hours=1):
        return redirect('logout')

    return render(request, 'central.html', context)

# CountDown
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editTime(request):
    if request.method == 'POST':
        timer = Timer.objects.get(id=request.POST.get('id'))
        if timer  != None:
            timer.timer = request.POST.get('timer')
            timer.save()
            messages.success(request, 'editado com sucesso')
            return HttpResponseRedirect('/central')
    
       
# efeito de digitacao
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editTyped(request):
    if request.method == 'POST':
        tiped = Tiped.objects.get(id=request.POST.get('id'))
        if tiped  != None:
            
            tiped.fixo = request.POST.get('fixo')
            tiped.txt01 = request.POST.get('txt01')
            tiped.txt02 = request.POST.get('txt02')
            tiped.txt03 = request.POST.get('txt03')
            tiped.txt04 = request.POST.get('txt04')
            
            tiped.save()
            messages.success(request, 'editado com sucesso')
            return HttpResponseRedirect('/central')

# efeito de Musica
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def song(request):
    if request.method == 'POST':
        sound = Music.objects.get(id=request.POST.get('id'))
        title_music = request.POST.get('title_music')  
        if title_music:  
            sound.title_music = title_music 
        
        if request.FILES.get('music') is not None:
            file = request.FILES['music']
            st = FileSystemStorage()
            x = st.save(file.name, file)
        else:
            x = None
        
        if x is not None:
            sound.music = x
        sound.save()
        messages.success(request, "editado com sucesso")
        return HttpResponseRedirect('/central')
#usar somente para manutencao
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def slide(request):
    if request.method == 'POST':
        form = ImagesForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "editado com sucesso")
            return HttpResponseRedirect('/central')
        else:
            return render(request,'add_img.html', {'form':form})
    else:
        form = ImagesForm
        return render(request,'add_img.html', {'form':form})

#editar slides
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update(request, id):
    s = Images.objects.get(pk=id)
    d = Padrao.objects.all()
    form = ImagesForm(request.POST or None, request.FILES or None, instance= s)
    if form.is_valid():
        s = form.save()
        s.save()
        messages.success(request,'editado com sucesso')
        return redirect('/central')
    context = {
        "s":s,
        "d":d,
        'form':form
    }
    return render(request, "update_img.html", context)

#HomePage
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editHome(request):
    if request.method == 'POST':
        home_id = request.POST.get('id')
        home = get_object_or_404(Home, id=home_id)

        # Lista de campos para atualizar
        fields = [
            'home_title', 'icon_title', 'horario',
            'card_title01', 'card_color01', 'card_icon01', 'txt_card_a1', 'txt_card_b1', 'txt_card_c1',
            'card_title02', 'card_color02', 'card_icon02', 'txt_card_a2', 'txt_card_b2', 'txt_card_c2',
            'btn_color', 'icon_type',
            'Modal_title', 'Modal_card_title', 'modal_card_color', 'modal_card_icon',
            'cargo01', 'cargo02', 'cargo03', 'cargo04', 'cargo05'
        ]

        # Atualizar os campos do objeto Home
        for field in fields:
            setattr(home, field, request.POST.get(field))

        home.save()

        messages.success(request, 'Editado com sucesso')

        return redirect(reverse('central'))
 
