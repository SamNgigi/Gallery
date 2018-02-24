from django.db import models
import datetime as dt
# Create your models here.


class Location(models.Model):
    # TODO: Will try geolocation
    location = models.CharField(max_length=60, blank=True, default='nairobi')

    def __str__(self):
        return self.location


class Category(models.Model):
    category = models.CharField(max_length=30, blank=True)

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.category


class Image(models.Model):
    image = models.ImageField(upload_to='gallery/', blank=True)
    image_url = models.TextField(blank=True)
    image_name = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=100, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    post_date = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(
        'Location', on_delete=models.CASCADE, blank=True)

    class Meta:
        ordering = ['-post_date']

    def save_image(self):
        self.save()

    @classmethod
    def get_all(cls):
        images = cls.objects.order_by('-post_date')
        return images

    @classmethod
    def today_pics(cls):
        today = dt.date.today()
        images = cls.objects.filter(post_date__date=today)
        return images

    @classmethod
    def get_by_category(cls):
        pass
