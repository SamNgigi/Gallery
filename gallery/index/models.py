from django.db import models

# Create your models here.


class Location(models.Model):
    pass


class Category(models.Model):
    pass


class Image(models.Model):
    image = models.ImageField(upload_to='gallery/')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    # location = models.ForeignKey(Location)
    # category = models.ForeignKey(Category)
