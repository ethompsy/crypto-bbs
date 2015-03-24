import datetime
from django.utils import timezone
from django.utils.timezone import utc
from django.db import models
from django.core.cache import cache

class Board(models.Model):
    key = models.TextField(blank=True)
    date = models.DateTimeField('created', auto_now_add=True)
    def __unicode__(self):
        return self.key
    class Meta:
        db_table = 'board'
        ordering = ['date']

class Post(models.Model):
    board = models.ForeignKey(Board, related_name='posts')
    date = models.DateTimeField('posted', auto_now_add=True)
    text = models.TextField(blank=True)
    def __unicode__(self):
        return self.date
    class Meta:
        db_table = 'post'
        ordering = ['date']