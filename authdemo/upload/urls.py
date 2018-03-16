from django.urls import path
from . import views

app_name = "upload"

urlpatterns = [
  path('<username>/', views.upload_page, name="upload_page"),
  path('<username>/upload', views.process_image_upload, name="upload")
]