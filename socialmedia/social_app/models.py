from django.db import models
from django.contrib.auth.models import User


class UserPost(models.Model):
    post_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    media_file = models.FileField(upload_to='media/posts-media', blank=True)
    date_posted = models.DateTimeField(auto_now=True)
    comments_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = "Posts"
    
    def __str__(self) -> str:
        return str(self.pk) + " | " + str(self.likes_count) + " Likes | " + str(self.comments_count) + " Comments"
 

class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.liker.username + " | " + str(self.parent_post.pk)
    
    
class Commment(models.Model):
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    content = models.TextField(max_length=100)
    date_commented = models.DateTimeField(auto_now=True)
    replies_count = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return str(self.pk) + " | " + self.commentor.username + " -> Post " + str(self.parent_post.pk)
    
    
class Reply(models.Model):
    parent_comment = models.ForeignKey(Commment, on_delete=models.CASCADE)
    replier = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=100)
    date_created = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Replies'
    
    def __str__(self) -> str:
        return str(self.pk) + " | " + self.replier.username + " -> Comment " + str(self.parent_comment.pk)
    
    
class Follower(models.Model):
    parent_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.follower.username + " -> " + self.parent_user.username
    
    
class Group(models.Model):
    group_name = models.CharField(max_length=40)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)
    member_count = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.group_name + " | " + " | " + self.owner.username + " | " + str(self.member_count) + " Members"
    
    
class GroupMember(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    group_joined = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Group Member'
        verbose_name_plural = 'Group Members'
    
    def __str__(self) -> str:
        return self.member.username + " -> Group " + self.group_joined.group_name + " | " + str(self.is_admin)
    
    
class Notification(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_received = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=150)
    viewed = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title + " -> " + self.owner.username + " | " + str(self.date_received)