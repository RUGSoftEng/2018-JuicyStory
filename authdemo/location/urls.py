from . import views
from django.urls import path

app_name = 'location'
urlpatterns = [
    path('list_images/', views.list_images, name='list_images')
]
