from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404
from .models import Chatgroup, Group_msg
import json
from django.template.loader import render_to_string
import datetime
from auth1.models import Users
from asgiref.sync import async_to_sync

class ChatroomConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['session'].get('username')
        print(self.user)

        self.chatroom_name = self.scope['url_route']['kwargs']['chatroom_name']
        
        try:
            self.chatroom_id = Chatgroup.objects.get(group_id=self.chatroom_name).group_id
            self.chatroom = Chatgroup.objects.get(group_id=self.chatroom_name)
            print(self.chatroom)
        except Chatgroup.DoesNotExist:
            self.close()
            return

        async_to_sync(self.channel_layer.group_add)(
            self.chatroom_name,
            self.channel_name
        )
        

        if self.user not in self.chatroom.users_online.all():
            id=Users.objects.get(username=self.user).id
            self.chatroom.users_online.add(id)
            self.update_online_count()


        self.accept()
        
    def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        body = text_data_json['body']

        print(body)
        
        username = self.scope['session'].get('username')
        if username is None:
            # Handle case where username is not in session
            return

        message = Group_msg.objects.create(
            body=body,
            username=username,
            group_id=self.chatroom_id,
            created=datetime.datetime.now()
        )

        print("created")
        print(message)
        
        event={
            'type':'message_handler',
            'message_id':message.id
        }
        async_to_sync(self.channel_layer.group_send)(
            self.chatroom_name,event
        )
        
    def message_handler(self, event):
        
        message_id=event['message_id']
        message=Group_msg.objects.get(id=message_id)
        context={
            'message':message,
            'user':self.scope['session'].get('username')
        }

        html=render_to_string("chat_message_p.html",context)
        print("Message send")
        self.send(text_data=html)

        
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.chatroom_name,
            self.channel_name
        )

        if self.user in self.chatroom.users_online.all():
            id=Users.objects.get(username=self.user)
            self.chatroom.users_online.remove(id)
            self.update_online_count() 

    def update_online_count(self):
        online_count = self.chatroom.users_online.count() - 1
        
        event = {
            'type': 'online_count_handler',
            'online_count': online_count
        }
        async_to_sync(self.channel_layer.group_send)(self.chatroom_name, event)


    def online_count_handler(self, event):
        online_count = event['online_count']
        
        chat_messages = Group_msg.objects.filter(group_id=self.chatroom.group_id)[:30]
        author_ids = set([message.username for message in chat_messages])
        users = Users.objects.filter(username__in=author_ids)
        
        context = {
            'online_count': online_count,
            'chat_group': self.chatroom,
            'users': users
        }
        html = render_to_string("online_count_p.html", context)
        self.send(text_data=html)
        

    