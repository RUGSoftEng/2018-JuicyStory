from . import views
from django.urls import path

app_name = 'statistics'

urlpatterns = [
  path('profile/', views.getViewsAndCount, name='getProfileStats'),
]