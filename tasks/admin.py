from .models import Task, Comment, Notification
from django.contrib import admin

admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Notification)