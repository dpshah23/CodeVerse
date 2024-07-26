from django.shortcuts import render,redirect
import datetime
from django.contrib import messages
import random 
import string
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
    
def signup( request):
    if request.method=="POST":
        username=request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        time_stamp = datetime.today()
        
        obj = Users_main(username = username , email=email ,user_id = user_id  , name = None , phone = None , city = None , qualification =None , profile_pic = None , dob = None , bio = None , description = None , time_stamp = time_stamp , is_active = False , level = None , tech = None)
        obj.set_password(password)
        obj.save()

    return render (request , 'next_user.html')