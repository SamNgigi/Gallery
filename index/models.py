from django.db import models
import datetime as dt
# Create your models here.


class Location(models.Model):
    # TODO: Will try geolocation
    location = models.CharField(max_length=60)

    def __str__(self):
        return self.location


class Category(models.Model):
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='gallery/', blank=True)
    image_url = models.TextField(blank=True)
    image_name = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=100, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    post_date = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(
        'Location', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-post_date']

    def save_image(self):
        self.save()

    @classmethod
    def get_all(cls):
        images = cls.objects.order_by('-post_date')
        return images

    @classmethod
    def searched(cls, query):
        # TODO: Remember to add more categories.
        result = cls.objects.filter(
            description__icontains=query).order_by('-post_date')
        return result

    @classmethod
    def today_pics(cls):
        today = dt.date.today()
        images = cls.objects.filter(post_date__date=today)
        return images

    @classmethod
    def get_architecture(cls):
        cat_images = cls.objects.filter(
            category__name__startswith='architecture').order_by('-post_date')
        return cat_images

    @classmethod
    def mombasa(cls):
        images = cls.objects.filter(
            location__location__startswith='mombasa').order_by('-post_date')
        return images

    @classmethod
    def nairobi(cls):
        images = cls.objects.filter(
            location__location__startswith='nairobi').order_by('-post_date')
        return images
