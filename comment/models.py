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

    STATUS_VISIBLE = 'visible'
    STATUS_HIDDEN = 'Hidden'
    STATUS_MODERATED = 'moderated'
    STATUS_CHOICES = (
        (STATUS_VISIBLE, 'Visible'),
        (STATUS_HIDDEN, 'Caché'),
        (STATUS_MODERATED, 'Moderé'),
    )
    status = models.CharField(max_length=20,
                              default=STATUS_VISIBLE,
                              choices=STATUS_CHOICES)
    moderation_text = models.CharField(max_length=250, blank=True)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        return '{} - {} (status={})'.format(self.name, self.content[:20], self.status)
