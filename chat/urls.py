from django.urls import path
from .views import *
urlpatterns = [
    path('',dispall,name="chatdisp"),
    path('<chatroom_name>/' , home_view , name='home'),
    path('join/<id>/',join,name="join"),
    path('chat/<username>' , get_or_create_chatroom , name="start-chat"),
    path('chat/room/<chatroom_name>' , dispall ,  name='chatroom'),
]
