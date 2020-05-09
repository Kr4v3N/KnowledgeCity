from django.db import models


# Create your models here.

class SubCategory(models.Model):

    name = models.CharField(max_length=50)
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sous-catégorie'
        verbose_name_plural = 'Sous-catégories'

