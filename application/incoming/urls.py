from django.urls import path
from .views import (select_images, list_images_view)

app_name = 'incoming'

urlpatterns = [
    path('add/', select_images, name='select_images'),
    path('', list_images_view, name='list_images')
]
