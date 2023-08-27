from .models import Notification

class NotificationService:
    def comment_notification(user):
        message = "Your post received a new comment!"
        return Notification.objects.create(message=message, owner=user)
    
    def reply_notification(user):
        message = "Your comment received a new reply!"
        return Notification.objects.create(message=message, owner=user)
    
    def follow_notification(user):
        message = f"{user.first_name} {user.last_name} followed you!"
        return Notification.objects.create(message=message, owner=user)