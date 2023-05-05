from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    post_type=models.IntegerField()
    title=models.CharField(max_length=50)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    time_stamp=models.DateTimeField(auto_now=True)
    content=models.TextField()
    image_url=models.CharField(max_length=50)
    likes=models.IntegerField()
    reports=models.IntegerField()

class Comment(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    time_stamp=models.DateTimeField(auto_now=True)
    content=models.TextField(max_length=500)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

class Tags(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    name=models.CharField(max_length=15)
