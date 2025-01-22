from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'Sindhu'})
def blog(request):
    return render(request,'blog.html')
def shop(request):
    return render(request,'shop.html')
def contact(request):
    return render(request,'contact.html')
def aboutme(request):
    return render(request,'aboutme.html')
