from django.db import models
from django.contrib.auth.hashers import make_password,check_password
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Visit(models.Model):
    page_visited = models.CharField(max_length=255, unique=True)
    visit_count = models.PositiveIntegerField(default=0)

    def __str__(self):
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
    name = models.CharField(max_length=100,null=True)
    username=models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    user_id = models.CharField(max_length=50)
    phone = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=50,null=True)
    qualification = models.CharField(max_length=100,null=True)
    profile_pic = models.TextField(null=True)
    dob = models.DateField(null=True)
    bio = models.TextField(null=True)
    description = models.TextField(null=True)
    time_stamp = models.DateField()
    is_active = models.BooleanField(default=True)
    level = models.CharField(max_length=50,choices=levels,blank=True,null=True)
    tech=models.CharField(max_length=150,choices=tech,blank=True,null=True)
    
    
    def __str__(self):
        return self.username
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)


    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
class resetpass(models.Model):
    email=models.EmailField(max_length=100)
    keys=models.TextField()
    usage=models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField(default=timezone.now() + timedelta(hours=1))

    def is_expired(self):
        return timezone.now() > self.expires_at

    def __str__(self):
        return self.email