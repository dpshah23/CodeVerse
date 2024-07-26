from django.db import models

# Create your models here.
class clg_info(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    phone = models.IntegerField()
    dept = models.CharField(max_length=100)
    timestamp=models.DateField(blank=True)
    
    def __str__(self):
        return self.name
