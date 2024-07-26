from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

# Create your views here.
def dispall(request):
    if 'email' and 'username' not in request.session:
        messages.error(request,"Login Required")
        return redirect('/auth/login')
    
    try:
        userisactive=Users_main.objects.get(username=request.session['username'])
        if userisactive.is_active:
            messages.error(request,"Some Unusual Activity Happend in your account . So We have Blocked Your Account")
            return redirect('/auth/login')
    except Users_main.DoesNotExist:
        messages.error(request,"Account Does Not Exist...")
        return redirect('/auth/login')
        
    username=request.session['username']

    channels=[]
    joined=Joined.objects.filter(username=username)
    for join in joined:
       
        channels.append(Chatgroup.objects.get(group_id=join.group_id))
    return render(request,"disp_all_channels.html",{'channels':channels})
    
