# api/urls.py
from django.urls import path
from .views import download_image

urlpatterns = [
    path('download/vesna/', download_image),
]

