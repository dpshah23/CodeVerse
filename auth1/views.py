from django.shortcuts import render

from django.contrib import messages

from .models import Users


# Create your views here.

def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            user=Users.objects.get(email=email)

            if not user.isactive:
                messages.error(request,"Some Unusual Activity Happend to your account . So We have Blocked Your Account")
                return render(request,"login.html")
            
            islogin=user.check_password(password)
            if user.email==email and islogin:
                pass
        except Users.DoesNotExist:
            messages.error(request,"User Does Not Exist..")
            return render(request,"login.html")
        
    return render(request,"login.html")