from . import views
from django.urls import path

app_name = 'statistics'

urlpatterns = [
  path('profile/', views.get_views_and_count, name='get_profile_stats'),
]