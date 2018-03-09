from . import views
from django.urls import path

app_name = 'authcode'
urlpatterns = [
  path('', views.get_auth_code, name='get_auth_code')
]