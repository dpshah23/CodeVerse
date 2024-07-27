from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from .models import *
from auth1.models import Users_main
import random
from django.contrib import messages
import json
import google.generativeai as genai
from dotenv import load_dotenv
import os
from django.views.decorators.csrf import csrf_exempt


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
        
def channels(request):
    return render(request,"channels.html")
        
        
def blog_disp(request , blog_id):
    
    try :
        author = Blog.objects.get(blog_id=blog_id).author
        head_title = Blog.objects.get(blog_id=blog_id).head_title
        title1 = Blog.objects.get(blog_id=blog_id).title1
        title2 = Blog.objects.get(blog_id=blog_id).title2
        title3 = Blog.objects.get(blog_id=blog_id).title3
        img1 = Blog.objects.get(blog_id=blog_id).img1
        img2 = Blog.objects.get(blog_id=blog_id).img2
        img3 = Blog.objects.get(blog_id=blog_id).img3
        content1 = Blog.objects.get(blog_id=blog_id).content1
        content2 = Blog.objects.get(blog_id=blog_id).content2
        content3 = Blog.objects.get(blog_id=blog_id).content3
        keyword1 = Blog.objects.get(blog_id=blog_id).keyword1
        keyword2 = Blog.objects.get(blog_id=blog_id).keyword2
        keyword3 = Blog.objects.get(blog_id=blog_id).keyword3
        
        data = {
            'author' : author ,
            'head_title' : head_title ,
            'title1'  : title1 ,
            'title2' : title2 ,
            'title3' : title3 ,
            'img1' : img1 ,
            'img2' : img2 ,
            'img3' : img3 ,
            'content1' : content1 ,
            'content2' : content2 ,
            'content3' : content3 ,
            'keyword1' : keyword1 ,
            'keyword2' : keyword2,
            'keyword3' : keyword3,
            
            
        }
        
        return render (request , 'blogs_disp.html' , {'data' : data})
    
    except Blog.DoesNotExist:
        messages.error("This blog does not exist")
        return redirect('/')
    except Exception as e :
        print(e)
        return redirect('/')
    
def all_blogs(request):
    pass


@csrf_exempt
def api_reply(request):
    if request.method=="POST":
        load_dotenv()
        api_key=os.getenv('API_KEY_GEMINI')
        data=json.loads(request.body)
        question = data.get('question', '')
        try:
            genai.configure(api_key=api_key)

            model = genai.GenerativeModel('gemini-pro')

            response = model.generate_content(question)

            return HttpResponse({'answer':response.text})

        except Exception as e:
            print(e)
            return HttpResponse({'error':False})