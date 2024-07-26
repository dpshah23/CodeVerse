from django.shortcuts import render

from django.contrib import messages


# Create your views here.

def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            user=Users.objects.get(email=email)

            if not user.isactive:
                messages.error(request,"")
        
    return render(request,"login.html")