from django.urls import path
from . import views

app_name = "upload"

urlpatterns = [
  path('list_selected_images/', views.list_selected_images, name='list_selected_images'),
  path('remove_selected_images/', views.remove_selected_images, name='remove_selected_images')
]