from django.db import models


# Create your models here.

class Main(models.Models):

    name = models.TextField()

    def __str__(self):
        return self.name

