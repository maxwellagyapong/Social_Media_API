from django.contrib import admin
from .models import *

admin.site.register(UserPost)
admin.site.register(Like)
admin.site.register(Commment)
admin.site.register(Reply)
admin.site.register(Follower)
admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(Notification)
admin.site.register(SharedPost)