from django.urls import path
from .views import *

urlpatterns = [
    
    path('',home, name='home'),  
    path('channels/',channels,name="channels"),
    # path('blogs/<blog_id>/' , blog_disp , name = 'blogs_display'),
    # path('blogs/' , all_blogs , name = 'all_blogs'),
    path('api/chatbot/',api_reply,name="api_reply"),
    path('profile/<username>',profile,name="profile"),
    path('checkansbeg/<username>',quiz_ans_beg,name="quiz_ans_beg"),
    path('checkansinter/<username>',quiz_ans_inter,name="quiz_ans_inter")

]
