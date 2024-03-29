from django.db import models
from django.contrib.auth.models import User
# from datetimeutc.fields import DateTimeUTCField
# from datetime import datetime

# Create your models here.

class classcreate(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    created=models.DateField(auto_now_add=True)
    classname = models.TextField(max_length=100)
    discription=models.TextField(max_length=200,blank=True,null=True)
    accessors=models.ManyToManyField(User,related_name='accessors')
    
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
    submition=models.TextField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.discription


    
class Submitedworks(models.Model):
    Message=models.TextField(max_length=300,blank=True,null=True)
    student=models.ForeignKey(User,on_delete=models.CASCADE,related_name='student')
    work=models.ForeignKey(Addwork,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='files', null=True, blank=True)
    status=models.BooleanField(default=False)

  

    






    
    



