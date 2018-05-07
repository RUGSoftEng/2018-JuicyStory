from django.urls import path
from . import views

app_name = 'iusers'

urlpatterns = [
	#path('addIuser/', views.add_iuser, name='add_iuser'),
	path('listIusers/', views.list_iusers, name='list_iusers'),
]