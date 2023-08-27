from django.db import models
from user_app.models import User


class UserPost(models.Model):
    post_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    media_file = models.FileField(upload_to='media/posts-media', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    comments_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = "Posts"
    
    def __str__(self) -> str:
        return f"{self.post_owner.first_name} {self.post_owner.last_name} | {self.content} | Likes: {self.likes_count} | Comments:  {self.comments_count}"
 

class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_post = models.ForeignKey(UserPost, on_delete=models.CASCADE, related_name='likes')
    
    class Meta:
        unique_together = ('liker', 'parent_post',)
    
    def __str__(self) -> str:
        return f"{self.liker.first_name} {self.liker.last_name}"
    
    
class Commment(models.Model):
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_post = models.ForeignKey(UserPost, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=100)
    date_commented = models.DateTimeField(auto_now_add=True)
    replies_count = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.content 
    
    
class Reply(models.Model):
    parent_comment = models.ForeignKey(Commment, on_delete=models.CASCADE, related_name='replies')
    replier = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Replies'
    
    def __str__(self) -> str:
        return self.content 
    
    
class Follower(models.Model):
    parent_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('parent_user', 'follower',)
    
    def __str__(self) -> str:
        return f"{self.follower.first_name} {self.follower.last_name} follows {self.parent_user.first_name} {self.parent_user.last_name}"
    
    
class Group(models.Model):
    group_name = models.CharField(max_length=40, unique=True)
    description = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    member_count = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.group_name + " | Members: " + str(self.member_count) 
    
    
class GroupMember(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group_members')
    date_joined = models.DateField(auto_now_add=True)
    is_group_admin = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('member', 'parent_group',)
        verbose_name = 'Group Member'
        verbose_name_plural = 'Group Members'
    
    def __str__(self) -> str:
        return f"{self.member.first_name} {self.member.last_name}"
    
    
class Notification(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_received = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=100)
    is_viewed = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.message + " | " + str(self.date_received)
    
    
class SharedPost(models.Model):
    original_post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    shared_by = models.ForeignKey(User, on_delete=models.CASCADE)
    time_shared = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.original_post.content