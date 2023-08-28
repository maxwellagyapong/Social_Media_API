from .models import Notification

class NotificationService:
    def comment_notification(user):
        message = "Your post received a new comment!"
        return Notification.objects.create(message=message, owner=user)
    
    def reply_notification(user):
        message = "Your comment received a new reply!"
        return Notification.objects.create(message=message, owner=user)
    
    def follow_notification(user):
        message = "You got a new follower!"
        return Notification.objects.create(message=message, owner=user)
    
    def share_notification(user):
        message = "Someone shared your post!"
        return Notification.objects.create(message=message, owner=user)