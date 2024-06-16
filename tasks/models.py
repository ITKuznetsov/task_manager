from django.db import models
from django.contrib.auth.models import User

from tasks.utils import AbstractModel


class Task(AbstractModel):
    PRIORITIES = (
        ('низкий', 'Низкий'),
        ('средний', 'Средний'),
        ('высокий', 'Высокий'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=False, null=False)
    deadline = models.DateTimeField()
    priority = models.CharField(max_length=50, choices=PRIORITIES)
    status  = models.CharField(max_length=50, choices=(
        ('выполнена', 'Выполнена'), 
        ('не выполнена', 'Не выполнена'), 
        ('в процессе', 'В процессе')
        ), 
        default='не выполнена')
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name='tasks')
    assigned_to = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name='assigned_tasks')


class Comment(AbstractModel):
    text = models.TextField()
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='comments')


class Notification(AbstractModel):
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE, related_name='notifications')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='notifications')
    is_sent = models.BooleanField(default=False)


