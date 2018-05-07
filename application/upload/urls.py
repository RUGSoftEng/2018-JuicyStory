from django.urls import path
from . import views

app_name = "upload"

urlpatterns = [
  path('list_selected_images/', views.list_selected_images, name='list_selected_images'),
  path('process_selected_images/', views.process_selected_images, name='process_selected_images')
]