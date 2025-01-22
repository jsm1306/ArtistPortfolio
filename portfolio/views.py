from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    gallery = Gallery.objects.all()
    return render(request, 'home.html', {'gallery': gallery})
def blog(request):
    return render(request,'blog.html')
def shop(request):
    return render(request,'shop.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        # For simplicity, just display a success message.
        return HttpResponse(f"Thank you for your message, {name}!")
    
    return render(request, "contact.html")
def aboutme(request):
    return render(request,'aboutme.html')
