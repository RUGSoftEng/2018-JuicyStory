from django.urls import path
from .views import (CreateUser, LoginUser, sign_up, log_in, log_out)

app_name = 'entry'

urlpatterns = [
	path('register-user/', CreateUser.as_view(), name='signup_user'),
	path('login-user/', LoginUser.as_view(), name='login_user'),
	path('signup/', sign_up, name='signup'),
	path('login/', log_in, name='login'),
	path('logout/', log_out, name='logout'),
]