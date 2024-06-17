from django.db import models
from django.contrib.auth.models import User

from tasks.utils import AbstractModel


class Task(AbstractModel):
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


    def __str__(self):
        return f"{self.title} | {self.assigned_to}"

    PRIORITIES = (
        ('низкий', 'Низкий'),
        ('средний', 'Средний'),
        ('высокий', 'Высокий'),
    )
    title = models.CharField(max_length=255, verbose_name='Задача')
    description = models.TextField(blank=False, null=False, verbose_name='Описание')
    deadline = models.DateTimeField(verbose_name='Дедлайн')
    priority = models.CharField(max_length=50, choices=PRIORITIES, verbose_name='Приоритет')
    status  = models.CharField(max_length=50, choices=(
        ('выполнена', 'Выполнена'), 
        ('не выполнена', 'Не выполнена'), 
        ('в процессе', 'В процессе')
        ), 
        default='не выполнена', verbose_name='Статус')
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name='tasks', verbose_name='Инициатор')
    assigned_to = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name='assigned_tasks', verbose_name='Исполнитель')


class Comment(AbstractModel):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


    def __str__(self):
        return f"{self.task} | {self.author}"
    
    text = models.TextField(verbose_name='Текст комментария')
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE, related_name='comments', verbose_name='Задача')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')


class Notification(AbstractModel):
    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'


    def __str__(self):
        return f"{self.task} | {self.user}"
    
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE, related_name='notifications', verbose_name='Задача')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='notifications', verbose_name='Пользователь')
    is_sent = models.BooleanField(default=False, verbose_name='Отправлено')


