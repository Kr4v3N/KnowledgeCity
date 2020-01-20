from django.db import models


# Create your models here.

class Main(models.Model):
    name = models.TextField()
    about = models.TextField()
    linkedin = models.TextField(default="-")
    facebook = models.TextField(default="-")
    twitter = models.TextField(default="-")
    youtube = models.TextField(default="-")
    github = models.TextField(default="-")
