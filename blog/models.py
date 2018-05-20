from django.db import models
from datetime import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 140)
    content = models.TextField(max_length = 1000)
    tags = models.CharField(max_length = 100 )
    timestamp = models.DateTimeField(default = datetime.now)
    author_id = models.IntegerField(default =-1)
    author_name = models.CharField(default= 'none', max_length=200)
    likes = models.IntegerField(default = 0)
    post_image = models.ImageField(blank = True, null = True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField(max_length = 1000)
    comment_author = models.CharField(max_length = 200, default='none')
    post_id = models.IntegerField(default=-1)
