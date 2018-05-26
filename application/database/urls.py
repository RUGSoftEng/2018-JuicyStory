from django.urls import path
from .views import FilterInstagramUser, RUDInstagramUser, CreateInstagramUser

app_name = 'database'

urlpatterns = [
	path('filter-iusers/', FilterInstagramUser.as_view(), name='filter-iuser'),
	path('create-iusers/', CreateInstagramUser.as_view(), name='create-iuser'),
	path('rud-iusers/<username>/', RUDInstagramUser.as_view(), name='rud-iuser'),
]