from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from news.models import News


class Blacklist(models.Model):
    ip = models.CharField(max_length=120)
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=12, default="00:00")

    class Meta:
        verbose_name = 'Blacklist'
        verbose_name_plural = 'Blacklists'

    def __str__(self):
        return self.ip
