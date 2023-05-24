from django.shortcuts import render
from django.contrib.auth.decorators import login_required # Login required to access private pagas
from django.views.decorators.cache import cache_control # Prevent back button (destroy the last section)

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