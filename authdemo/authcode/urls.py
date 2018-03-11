from . import views
from django.urls import path

app_name = 'authcode'
urlpatterns = [
    path('get_code', views.get_code, name='get_code'),
    path('receive_code', views.process_auth_code, name='process_auth_code'),
    path('user_list', views.user_list, name='user_list'),
]
