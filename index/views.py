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
