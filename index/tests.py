from django.test import TestCase
from . models import Location, Category, Image
import datetime as dt

# Create your tests here.


class LocationTestClass(TestCase):
    def setUp(self):
        self.test_location = Location(location="nairobae")

    def test_instance(self):
        self.asserTrue(isinstance(self.test_location, Location))

    def test_saving_location(self):
        self.test_location.save_locations()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_deleting_locations(self):
        self.test_location = Location(location="nairobae")
        self.test_location.save_locations()
        self.test_location.delete_locations()
        locations = Location.objects.all()
        self.assertTrue(len(locations) < 1)

    def test_updating_image(self):
        self.test_location = Location(location="nairobae")
        self.test_location.save_locations()
        updated = Location.update_location(1, 'nairobi')
        self.assertTrue(updated, 'nairobi')


class ImageTestClass(TestCase):
    def setUp(self):
        # Location
        self.test_location = Location(location="nairobae")
        self.test_location.save()
        # Category
        self.test_category = Category(category="people")
        self.test_category.save()
        # Image
        self.test_image = Image(image="testImage",
                                image_url="testImageurl",
                                image_name="Test",
                                description="This is a test",
                                location=self.test_location)
        self.test_image.save()
        self.test_image.category.add(self.test_category)

    def test_instance(self):
        self.asserTrue(isinstance(self.test_image, Image))

    def test_saving_image(self):
        self.test_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_deleting_image(self):
        self.test_image = Image(location="nairobae")
        self.test_image.save_image()
        self.test_image.delete_locations()
        locationss = Image.objects.all()
        self.assertTrue(len(locationss) < 1)

    def test_updating_image(self):
        self.test_image = Image(location="nairobae")
        self.test_image.save_image()
        updated = Image.update_image(1, 'image_name', "This test")
        self.assertTrue(updated, 'This test')


class CategoryTestClass(TestCase):
    def setUp(self):
        self.test = Category(category="people")

    def test_instance(self):
        self.asserTrue(isinstance(self.test, Image))

    def test_saving_category(self):
        self.test.save_category()
        images = Category.objects.all()
        self.assertTrue(len(images) > 0)

    def test_deleting_category(self):
        self.test = Category(category="people")
        self.test.save_category()
        self.test.delete_locations()
        locationss = Category.objects.all()
        self.assertTrue(len(locationss) < 1)

    def test_updating_category(self):
        self.test = Category(location="people")
        self.test.save_category()
        updated = Category.update_category(1, 'life')
        self.assertTrue(updated, 'life')
