from django.db import models

# Create your models here.
class clg_info(models.Model):
    
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    phone = models.IntegerField()
    dept = models.CharField(max_length=100)
    timestamp=models.DateField(blank=True)
    
    def _str_(self):
        return self.name

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
class Quiz(models.Model):
    

    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100 , blank = True)
    option2 = models.CharField(max_length=100 , blank = True)
    option3 = models.CharField(max_length=100 , blank = True)
    option4 = models.CharField(max_length=100 , blank = True)
    ans = models.CharField(max_length=100 , blank = True)
    level = models.CharField(max_length=50,choices=levels)
    tech=models.CharField(max_length=150,choices=tech,blank=True)
    
    def _str_(self):
        return self.question
    
class Blog(models.Model):
    author = models.CharField(max_length=100)
    blog_id = models.CharField(max_length=100)
    head_title = models.CharField(max_length=200)
    title1 = models.TextField()
    title2 = models.TextField(blank=True)
    title3 = models.TextField(blank=True)
    img1 = models.TextField( blank = True)
    img2 = models.TextField( blank = True)
    img3 = models.TextField( blank = True)
    content1 = models.TextField()
    content2 = models.TextField(blank=True)
    content3 = models.TextField(blank=True)
    keyword1 = models.CharField(max_length= 100)
    keyword2 = models.CharField(max_length= 100 , blank=True)
    keyword3 = models.CharField(max_length= 100 , blank=True)
    time_stamp = models.DateField()
    
    def __str__(self):
        return self.head_title
    
