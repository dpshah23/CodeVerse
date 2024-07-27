from django.urls import path
from .views import *

urlpatterns = [
    
    path('',home, name='home'),  
    path('channels/',channels,name="channels"),
    path('blogs/<blog_id>/' , blog_disp , name = 'blogs_display'),
    path('blogs/' , all_blogs , name = 'all_blogs'),
]
