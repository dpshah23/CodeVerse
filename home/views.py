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
        tech =  Users_main.objects.get(email=email).tech
        questions = Quiz.objects.filter(level=level , tech=tech)
        final = random.sample(questions, 5) 
            
        print(final)
    
                
                
    except Exception as e:
        print(e)
    return HttpResponse("hello")

def quiz_ans_beg(request):
    
    email = request.session['email']
    level =  Users_main.objects.get(email=email).level
    if level == "begineer":
        if request.method=="POST":
                
            ans1 = request.POST.get('ans1')
            q1= request.POST.get('q1')

            ans2 = request.POST.get('ans2')
            q2 = request.POST.get( 'q2')

            ans3 = request.POST.get('ans3')
            q3 = request.POST.get( 'q3')
            
            ans4 = request.POST.get('ans4')
            q4 = request.POST.get( 'q4')
            
            ans5 = request.POST.get('ans5')
            q5 = request.POST.get( 'q5')
            final_ans = []
            
            if ans1 == Quiz.objects.get(id=q1).ans :
                final_ans.append()
            if ans2 == Quiz.objects.get(id = q2).ans :
                final_ans.append()
            if ans3 == Quiz.objects.get(id = q3).ans :
                final_ans.append()
            if ans4 == Quiz.objects.get(id = q4).ans :
                final_ans.append()
            if ans5 == Quiz.objects.get(id = q5).ans :
                final_ans.append()
            
        
            return render(request,"get_score.html",{'score':len(final_ans)}) 
        
        