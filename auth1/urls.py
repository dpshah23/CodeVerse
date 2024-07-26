from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login,name="login"),
    path('check_user/<username>/',check_user,name="check_user")
]
