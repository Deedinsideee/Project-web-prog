import urllib
from urllib.parse import quote_from_bytes

from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50, null=True)
    anons = models.CharField('Анонс', max_length=250, null=True)
    full_text = models.TextField('Статья', null=True)
    time = models.DateTimeField('Дата публикации', null=True)
    counter = 0

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'


    def update_counter(self):
        self.counter + 1


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
