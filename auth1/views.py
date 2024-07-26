from django.shortcuts import render,redirect

from django.contrib import messages

from .models import Users_main
from django.http import HttpResponse

# Create your views here.

def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            user=Users_main.objects.get(email=email)

            if not user.isactive:
                messages.error(request,"Some Unusual Activity Happend in your account . So We have Blocked Your Account")
                return render(request,"login.html")
            
            islogin=user.check_password(password)
            if user.email==email and islogin:
                
                request.session['username']=user.username
                request.session['email']=user.email
                request.session['name']=user.name
                request.session['id']=user.user_id

                return redirect('/')

            else:
                messages.error(request,"Incorrect Password ....")
                return redirect('/auth/login')
        except Users_main.DoesNotExist:
            messages.error(request,"User Does Not Exist..")
            return render(request,"login.html")
        
    return render(request,"login.html")

def check_user(request,username):
    try:
        user=Users_main.objects.get(username=username)
        return HttpResponse({"success":False})
    except Users_main.DoesNotExist:
        return HttpResponse({"success":True})