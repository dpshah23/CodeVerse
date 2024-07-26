from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from .models import clg_info

# Create your views here.
def home(request):
    return render(request,"home.html")

def clg_info(request):
    if request.method=="POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        dept=request.POST.get('dept')
        
        date=datetime.today()
        
        
        obj=clg_info(name=name,address=address,email=email,phone=phone,dept=dept,timestamp=date)
        obj.save()
        
    return redirect('/')
        
def quiz (request):
    try:
    except:
        pass
    return render(request,"quiz.html")