from django.db import models


# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=200)
    short_txt = models.TextField()
    body_txt = models.TextField()
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=12, default="00:00")
    pic_name = models.TextField(default="-")
    pic_url = models.TextField(default="-")
    writer = models.CharField(max_length=50)
    category_name = models.CharField(max_length=50, default="-")
    category_id = models.IntegerField(default=0)
    ocategory_id = models.IntegerField(default=0)
    show = models.IntegerField(default=0)
    tag = models.TextField(default="")
    activated = models.IntegerField(default=0)
    rand = models.TextField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
