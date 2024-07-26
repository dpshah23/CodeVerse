from django.contrib import admin
from .models import Chatgroup,Group_msg,Joined

# Register your models here.


admin.site.register(Chatgroup)
admin.site.register(Group_msg)
admin.site.register(Joined)