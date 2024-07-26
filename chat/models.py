from django.db import models
# from django.contrib.auth.models import User
from auth1.models import *
from datetime import datetime
import django.utils.timezone

# Create your models here.
class Chatgroup(models.Model):
    group_id=models.CharField(max_length=150,default=None,null=True)
    group_name = models.CharField(max_length= 100 , unique=True)
    users_online = models.ManyToManyField(Users_main , related_name='online_in_groups', blank=True)
    
    
    def __str__(self):
        return self.group_name
    
class Joined(models.Model):
    username = models.CharField(max_length=150,null=True)
    email = models.CharField(max_length=150,null=True)
    group_id=models.CharField(max_length=150,null=True , default=None)
    timestamp=models.DateField(default=None,null=True)
    profile_pic=models.TextField(blank=True,null=True)
    

    def __str__(self) -> str:
        return self.email
class Group_msg(models.Model):
    group_id = models.CharField(max_length=150,default=None,null=True)
    username = models.CharField(max_length=150)
    body = models.TextField( blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(Joined, on_delete=models.CASCADE, related_name='messages',blank=True,null=True)
    

    def get_profile_pic(self):
        try:
            joined = Users_main.objects.get(username=self.username)
            return joined.profile_pic
        except Joined.DoesNotExist:
            return None
        

    def __str__(self):
       
        return f"Message by {self.username} in group {self.group_id}: {self.body[:20]}..."
    
        
    class Meta:
        ordering = ['-created']