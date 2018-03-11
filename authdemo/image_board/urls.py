from . import views
from django.urls import path

app_name = 'image_board'
urlpatterns = [
    path('<username>/', views.list_images, name='list_images')
]
