from . import views
from django.urls import path

app_name = 'statistics'

urlpatterns = [
	path('get-fbtoken/', views.get_token, name='somename'),
	path('redirect/', views.fbtoken_redirect),
]	