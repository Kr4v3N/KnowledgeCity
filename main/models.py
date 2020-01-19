from django.db import models


# Create your models here.

class Main(models.Model):

    name = models.TextField()

    class Meta:
        verbose_name = 'Principale'
        verbose_name_plural = 'Principaux'

    def __str__(self):
        return self.name


