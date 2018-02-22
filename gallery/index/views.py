from django.shortcuts import render

"""
Create your views here.
We need to first define our app in the
project folder settings 'INSTALLED APPS', before displaying
them.
"""


def index(request):
    title = 'Welcome'
    test = 'Working!'
    return render(request, 'index.html', {"title": title, "test": test})
