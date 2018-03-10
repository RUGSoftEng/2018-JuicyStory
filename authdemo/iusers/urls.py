from django.urls import path
from . import views

app_name = 'iusers'

urlpatterns = [
	path('addIuser/', views.addIuser, name='addIuser'),
]