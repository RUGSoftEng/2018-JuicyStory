from django.urls import path, include
from rest_framework_jwt.views import (obtain_jwt_token, verify_jwt_token)
from incoming.views import IncomingDMs
from database.views import (FilterInstagramUser, RUDInstagramUser, CreateInstagramUser)
from entry.views import (CreateUser, LoginUser)
from statistics.views import (FilterInstagramUserStatistics, InstagramStoryUrls, InstagramStoryMetrics)
from upload.views import PostImageToStory
from .routers import router


app_name = 'api'

urlpatterns = [
  path('', include(router.urls)),

  path('get-token/', obtain_jwt_token, name='post-token'),
  path('verify-token/', verify_jwt_token, name='post-verify-token'),

  path('get-dms/<iusername>/', IncomingDMs.as_view(), name='get-instagram-dms'),

  path('filter-iusers/', FilterInstagramUser.as_view(), name='get-iuser'),
  path('create-iusers/', CreateInstagramUser.as_view(), name='post-iuser'),
  path('rud-iusers/<username>/', RUDInstagramUser.as_view(), name='get-put-delete-iuser'),

  path('register-user/', CreateUser.as_view(), name='post-register-user'),
  path('login-user/', LoginUser.as_view(), name='post-login-user'),

  path('stats/<iusername>/<timeStampSince>/<timeStampUntil>/',FilterInstagramUserStatistics.as_view(),name='get-account-statistics'),
  path('story/<iusername>/', InstagramStoryUrls.as_view(), name='get-story-images'),
  path('metrics/<iusername>/', InstagramStoryMetrics.as_view(), name='get-story-matrics'),

  path('post-story/', PostImageToStory.as_view(), name='post-image-to-story'),
]
