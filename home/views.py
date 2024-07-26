from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from .models import *
from auth1.models import Users_main
import random

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
        email = request.session['email']
        level =  Users_main.objects.get(email=email).level
        questions = Quiz.objects.filter(level=level)
        question1=[]
        final=[]
        
        for question in range(5):
            
            nq=random.choices(questions)
            if nq not in question1:
                final.append(nq)
                
        print(final)
                

    except Exception as e:
        print(e)
    return HttpResponse("hrllo")