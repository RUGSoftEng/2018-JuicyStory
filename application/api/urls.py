from django.urls import path, include
from .routers import router
from rest_framework_jwt.views import (obtain_jwt_token, verify_jwt_token)
from database.views import (FilterInstagramUser, RUDInstagramUser, CreateInstagramUser)
from entry.views import (CreateUser, LoginUser)
from statistics.views import FilterInstagramUser

app_name = 'api'

urlpatterns = [
	path('', include(router.urls)),

	path('get-token/', obtain_jwt_token, name='post-token'),
    path('verify-token/', verify_jwt_token, name='post-verify-token'),

	path('filter-iusers/', FilterInstagramUser.as_view(), name='get-iuser'),
	path('create-iusers/', CreateInstagramUser.as_view(), name='post-iuser'),
	path('rud-iusers/<username>/', RUDInstagramUser.as_view(), name='get-put-delete-iuser'),

	path('register-user/', CreateUser.as_view(), name='post-register-user'),
	path('login-user/', LoginUser.as_view(), name='post-login-user'),

	path('<iusername>/<timeStampSince>/<timeStampUntil>/', FilterInstagramUser.as_view(), name='get-account-statistics'),


]

