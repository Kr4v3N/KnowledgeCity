from django.db import models


# Create your models here.

class Main(models.Model):
    name = models.TextField()
    about = models.TextField()
