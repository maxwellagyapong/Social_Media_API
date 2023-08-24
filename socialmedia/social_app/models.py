from django.db import models
from django.contrib.auth.models import User


class UserPost(models.Model):
    post_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    media_file = models.FileField(upload_to='', blank=True)
    date_posted = models.DateTimeField(auto_now=True)
    comments_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
 

class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    
    
