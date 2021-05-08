from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date

# Create your models here.

class classcreate(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    created=models.DateField(auto_now_add=True)
    classname = models.TextField(max_length=100)
    discription=models.TextField(max_length=200)
    
    def __str__(self):
        return self.classname
    

def upload_path(instance,filename):
    return '/'.join(['files',str(instance.discription),filename])

class Addwork(models.Model):
    discription=models.TextField(max_length=200)
    auther=models.ForeignKey(User,on_delete=models.CASCADE,related_name='auther')
    room=models.ForeignKey(classcreate,on_delete=models.CASCADE)
    created=models.DateField(auto_now_add=True)
    file = models.FileField(upload_to=upload_path, null=True, blank=True)


    
    



