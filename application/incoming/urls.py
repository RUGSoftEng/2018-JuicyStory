from django.urls import path
from . import views

app_name = 'incoming'

urlpatterns = [
    path('add/', views.select_images, name='select_images'),
    path('', views.list_images, name='list_images')
]
