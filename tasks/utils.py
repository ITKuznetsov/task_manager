'''
Файл для асбтрактных моделей

Асбтрактные модели не будут обрабатываться во время миграции
'''

from django.db import models


class AbstractModel(models.Model):
    class Meta:
        abstract = True

    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    def __str__(self):
        return f'{self.__class__.__name__} {self.pk}'