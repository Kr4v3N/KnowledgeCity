from django.db import models


# Create your models here.

class Newsletter(models.Model):
    email = models.EmailField(max_length=100, blank=True, unique=True)
    status = models.IntegerField()
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=12, default="00H00")
    phone_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'
