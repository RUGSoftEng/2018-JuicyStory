from django.urls import path
from . import views

app_name = "upload"

urlpatterns = [
  path('<username>/', views.upload_page, name="upload_page"),
]