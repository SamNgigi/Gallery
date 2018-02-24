from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='welcome'),
    path('architecture', views.architecture, name='architecture'),
]
"""
We first import the project settings where we added the
template context processor that allows us to load our images.

We also add the static function from django.conf.urls.static.

We configure our app url to register the MEDIA_ROOT route.
"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
