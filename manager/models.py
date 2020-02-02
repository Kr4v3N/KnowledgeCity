from django.db import models


# Create your models here.

class Manager(models.Model):
    name = models.CharField(max_length=50)
    user_txt = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Direction'
        verbose_name_plural = 'Directions'
