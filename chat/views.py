from django.shortcuts import render

# Create your views here.
def viewdisp(request):
    username=request.session['username']

    channels=[]
    joined=Joined.objects.filter(username=username)
    for join in joined:
       
        channels.append(Chatgroup.objects.get(group_id=join.group_id))
    return render(request,"disp_all_channels.html",{'channels':channels})
    
    pass