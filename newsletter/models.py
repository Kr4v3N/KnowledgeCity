from django.db import models


# Create your models here.

class Newsletter(models.Model):
    txt = models.CharField(max_length=50)
    status = models.IntegerField()
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=12, default="00:00")

    def __str__(self):
        return self.txt

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'
