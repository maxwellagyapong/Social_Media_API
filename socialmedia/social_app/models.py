from django.db import models
from django.contrib.auth.models import User


class UserPost(models.Model):
    post_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    media_file = models.FileField(upload_to='')
    date_posted = models.DateTimeField(auto_now=True)
    comments_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    