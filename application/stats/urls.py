from . import views
from django.urls import path

app_name = "stats"

urlpatterns = [
  #path('', views.getProfileStats, name='getProfileStats'),
  path('test/', views.somePage, name='somePage'),
]