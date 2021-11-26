from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):  
    student_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10)  
    email = models.EmailField()
   
    def __str__(self):  
        return "%s %s" % (self.first_name, self.last_name)  
