from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Frontend
    path('', views.frontend, name="frontend"),
    path('offer', views.offer, name="offer"),
    # Backend
    path('backend/', views.backend, name="backend"),
    path('Inbox/', views.Inbox name="Inbox")
    # Login/Logout
    path('login/', include('django.contrib.auth.urls')),
]
