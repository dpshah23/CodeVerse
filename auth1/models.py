from django.db import models
from django.contrib.auth.hashers import make_password,check_password
from django.utils import timezone

# Create your models here.
class Visit(models.Model):
    page_visited = models.CharField(max_length=255, unique=True)
    visit_count = models.PositiveIntegerField(default=0)

    def _str_(self):
        return f"{self.page_visited} - {self.visit_count}"

levels=(
    ("BEGINNER","begineer"),
    ("INTERMEDIATE","intermediate"),
    ("EXPERT","expert"),
)
tech=(
    ("FRONTEND","frontend"),
    ("BACKEND","backend"),
    ("MOBILEAPP","mobileapp"),
    ("DATA SCIENCE","datascience"),
    ("ARTIFICIAL INTELLIGENCE/MACHINE LEARNING","ai/ml"),
    ("GAME DEVELOPMENT","gamedev")
    
)

class Users_main(models.Model):
    name = models.CharField(max_length=100)
    username=models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    user_id = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    qualication = models.CharField(max_length=100)
    profile_pic = models.TextField()
    dob = models.DateField()
    bio = models.TextField()
    desciption = models.TextField()
    time_stamp = models.DateField()
    is_active = models.BooleanField(default=True)
    level = models.CharField(max_length=50,choices=levels,blank=True)
    tech=models.CharField(max_length=150,choices=tech,blank=True)
    
    
    def _str_(self):
        return self.name
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)


    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    