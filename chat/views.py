from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import ChatmessageCreateForm 
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token


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
    

@csrf_exempt
def home_view(request , chatroom_name):
    if 'email' not in request.session:
        return redirect('/auth/login')
    
    try:
        obj=Chatgroup.objects.get(group_id=chatroom_name)
        print(obj)
    except Exception as e:
        messages.error(request,"Channel Not Found...")
        print(e)
        return redirect('/chat')
        
    email=request.session['email']
    username=request.session['username']
    print(email)
    
    requestusers=Joined.objects.filter(email=email).count()
    
    # print(requestusers)
    
    
    if (requestusers>0):
        pass
    else:
        return redirect(f"/chat/join/{chatroom_name}") 
    
    
    # chat_group = get_object_or_404(Chatgroup, group_name=chatroom_name)
    # chat_messages = chat_group.chat_messages.all()[:30]
    
    chat_group=Chatgroup.objects.get(group_id=chatroom_name)
    print(chat_group.group_name)
    chat_messages=Group_msg.objects.filter(group_id=chatroom_name)[:30]

    print(chat_messages)
    form = ChatmessageCreateForm()
    if request.method == 'POST' and request.htmx:
        form=ChatmessageCreateForm(request.POST)
        if form.is_valid():
            message=form.save(commit=False)
            message.username=request.session['username']
            message.group_id=chatroom_name  
            message.save()

            joinedgrp=Joined.objects.get(group_id=message.group_id,username=message.username).profile_pic

            username=request.session['usename']
            context={
                'message':message,
                'user':username,
                'image': joinedgrp
            }
            return render(request,'chat_message_p.html',context)
    

    context = {
        'chat_messages' : chat_messages, 
        'form' : form,
        'chatroom_name' : chatroom_name,
        'chat_group' : chat_group,
        'csrf_token': get_token(request) if request.method == 'POST' else None,
        'user':request.session['username']

    
    }
    return render (request , 'chat.html' , context)

def join(request,id):
    if 'email' and 'username' not in request.session:
        messages.error(request,"Please Login")
        return redirect("/auth/login")
    
    if request.method=="POST":
        username=request.session['username']
        email=request.session['email']

        usercreate=Joined(username=username,email=email,group_id=id,timestamp=datetime.today())

        usercreate.save()

    return render(request,"accept_invite.html")

