from django.db import models
from datetime import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

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
    comment_to_post_author_id = models.IntegerField(default =-1 )
    post_id = models.IntegerField(default=-1)


class Like(models.Model):
    like_flag = models.BooleanField(default = False)
    like_author_id = models.IntegerField(default = -1)
    like_to_post_author_id = models.IntegerField(default =-1 )
    like_post_id = models.IntegerField(default = -1)
    like_author = models.CharField(max_length = 200, default='none')

class Question(models.Model):
    question = models.TextField(max_length = 500)
    question_post_id = models.IntegerField(default = -1, null = False)
    question_author_id = models.IntegerField(default = -1, null = False)
    question_asker = models.CharField(max_length = 200)
    answer_flag = models.BooleanField(default = False)

class Answer(models.Model):
    question_id = models.IntegerField(default = -1, null = False)
    answer = models.TextField(max_length = 1000, default = 'No Answer')


class Notification(models.Model):
    title = models.CharField(max_length = 256)
    message = models.TextField()
    by = models.CharField(max_length=200, default='none')
    viewed = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, **kwargs):
    if kwargs.get('created',False):
        Notification.objects.create(user_id = instance.comment_to_post_author_id, title="Comment-Notification",message=instance.comment, by=instance.comment_author)
