from django.db import models

# Create your models here.
class User(models.Model):
    email=models.EmailField(unique=True,max_length=50)
    password=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.email

class Secretory(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    flat_No=models.CharField(max_length=10)
    username=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    society_address=models.CharField(max_length=50)
    pic=models.FileField(upload_to='media/images',default='media/user.png',blank=True,null=True)
    
    
    
    def __str__(self):
        return self.username
    
class Member(models.Model):
    user_id=models.CharField(max_length=50)
    flat_No=models.CharField(max_length=10)
    username=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    society_address=models.CharField(max_length=50)
    pic=models.FileField(upload_to='media/images',default='media/user.png')
    
    
    
    def __str__(self):
        return self.username
    
class Notice(models.Model):
    user_id=models.ForeignKey(Secretory,on_delete=models.CASCADE)
    notice_of_title=models.CharField(max_length=250)
    notice_desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    pic=models.FileField(upload_to='media/images',default='media/notice.gif')
    
    def __str__(self):
        return self.notice_of_title
    
class Event(models.Model):
    user_id=models.ForeignKey(Secretory,on_delete=models.CASCADE)
    event_of_title=models.CharField(max_length=250)
    event_desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    pic=models.FileField(upload_to='media/images',default='media/event.png')
    
    def __str__(self):
        return self.event_of_title
    
