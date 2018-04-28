from . import views
from django.urls import path

app_name = 'authentication'
urlpatterns = [
    path('get_code', views.get_code, name='get_code'),
    path('receive_code', views.process_auth_code, name='process_auth_code'),
]
