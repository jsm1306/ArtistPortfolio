from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    gallery = Gallery.objects.all()
    return render(request, 'home.html', {'gallery': gallery})
def blog(request):
    return render(request,'blog.html')
def shop(request):
    return render(request,'shop.html')
def contact(request):
    return render(request,'contact.html')
def aboutme(request):
    return render(request,'aboutme.html')
