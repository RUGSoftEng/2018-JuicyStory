from . import views
from django.urls import path

app_name = 'incoming'
urlpatterns = [
    path('list_images/add/', views.select_images, name='select_images'),
    path('list_images/', views.list_images, name='list_images'),
    path('list_selected_images/', views.list_selected_images, name='list_selected_images'),
    path('remove_selected_images/', views.remove_selected_images, name='remove_selected_images')
]
