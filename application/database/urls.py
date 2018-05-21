from django.urls import path
from .views import FilterInstagramUser, RUDInstagramUser

app_name = 'database'

urlpatterns = [
	path('filter-iusers/', FilterInstagramUser.as_view(), name='filter-iuser'),
	path('rud-iusers/<username>/', RUDInstagramUser.as_view(), name='create-iuser'),
]