from django.shortcuts import render
from .models import Image
import datetime as dt
"""
Create your views here.
We need to first define our app in the
project folder settings 'INSTALLED APPS', before displaying
them.
"""


def index(request):
    title = 'Welcome'
    test = 'Working!'
    date = dt.date.today
    photos = Image.get_all()
    return render(request, 'index.html',
                  {"title": title,
                   "test": test,
                   "date": date,
                   "photos": photos})


def image(request, image_id):
    image = Image.objects.get(id=image_id)
    return render(request, 'image.html', {"image": image})


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        query = request.GET.get("image")
        results = Image.searched(query)
        message = f"{query}"

        return render(request, 'results.html',
                      {"message": message, "results": results})
    else:
        message = "What images do you want to search for?"
        return render(request, 'results.html',
                      {"message": message})


def get_mombasa(request):
    location_images = Image.mombasa()
    return render(request, 'locations.html', {"images": location_images})


def get_nairobi(request):
    location_images = Image.nairobi()
    return render(request, 'locations.html', {"images": location_images})


def architecture(request):
    title = 'Architecure'
    test = 'Architecure!'
    date = dt.date.today
    architecture = Image.get_architecture()
    return render(request, 'architecture.html',
                  {"title": title,
                   "test": test,
                   "date": date,
                   "architecture": architecture})
