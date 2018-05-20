from django.urls import path
from .views import InstagramUserView

app_name = 'database'

urlpatterns = [
	path('InstagramUserFilter', InstagramUserView.as_view(), name='test-api'),
]