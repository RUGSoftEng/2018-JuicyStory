from django.urls import path
from . import views

app_name = 'iusers'

urlpatterns = [
	path('listIusers/', views.list_iusers, name='list_iusers'),
]