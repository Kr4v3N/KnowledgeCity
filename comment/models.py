from django.db import models


# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=50)
    news_id = models.IntegerField(max_length=50)
    email = models.EmailField()
    comment_txt = models.TextField()
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'
