from . import views
from django.urls import path
from .views import FilterInstagramUser

app_name = 'statistics'

urlpatterns = [
  path('profile/<timeStampSince>/<timeStampUntil>/', views.get_views_and_count, name='get_profile_stats'),
  path('<timeStampSince>/<timeStampUntil>/', FilterInstagramUser.as_view(), name='somename'),
]