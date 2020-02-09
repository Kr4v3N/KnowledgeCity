from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from news.models import News

class Comment(models.Model):

    name = models.CharField(max_length=70)
    email = models.EmailField()
    content = models.TextField()
    news_id = models.IntegerField()
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=10)
    created = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        return self.name
