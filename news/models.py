from django.db import models


# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=50)
    short_text = models.TextField()
    body_text = models.TextField()
    date = models.CharField(max_length=12)
    pic = models.TextField()
    writer = models.CharField(max_length=50)
    category_name = models.CharField(max_length=50, default="-")
    category_id = models.IntegerField(default=0)
    show = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
