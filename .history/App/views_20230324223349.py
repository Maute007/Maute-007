from django.shortcuts import render
#new import
from django.contrib.auth.decorators import login_required # Login required to access private pagas
from django.views.decorators.cache import cache_control # Prevent back button (destroy the last section)
from django.http import HttpResponseRedirect #REDIRECT AFTER SUMIT 
from django.contrib import messages 
from django.core.mail import EmailMultiAlternatives #REQUIRED TO SEND EMAIL
from django.template import loader # RENDER TEMPLATE ON EMAIL


# Frontend
def frontend(request):
    return render(request, "frontend.html")

# Frontend
def offer(request):
    return render(request, "offer.html")
# Backend
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def backend(request):
    return render(request, "backend.html")

# Frontend
def Inbox(request):
    return render(request, "Inbox.html")

#============== Send email====================================
def email_count(request):
    if request == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address= request.POST.get('address')
        exp = request.POST.get('exp')
        skills = request.POST.get('skills')
       
        template = loader.get_template('resume_form.txt')
        context = {
           'name' : name,
           'age' : age,
           'email' : email,
           'phone' : phone,
           'address' : address,
           'exp' : exp,
           'skills' : skills
        }
        message = template.render(context)
        email = EmailMultiAlternatives(
           "Counter - Candidate",
           "Counter - Opportunity",
           ['carlxyzsmaute@gmail.com']
        )
        email.content_subtype = 'html'
        file = request.FILES['file']
        email.attach(file.name, file.read(), file.content_type)
        email.send()
        messages.success(request, 'Counter resume sent successfully !')
        return HttpResponseRedirect("/")
