from . import views
from django.urls import path

app_name = 'authcode'
urlpatterns = [
  path('', views.process_auth_code, name='process_auth_code'),
  path('user_list', views.user_list, name='user_list'),
  # path('send_auth_request', views.send_auth_request, name='send_auth_request')
]