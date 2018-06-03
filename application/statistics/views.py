from database.models import InstagramUser
from django.shortcuts import get_object_or_404
# from .utils import *
from .utils import request_views_and_followers, request_story_stats, request_story_urls
from .serializers import InstagramUserSerializer

from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.views import APIView


class FilterInstagramUserStatistics(APIView):
  ''' Api for setting filters based on the field attributes below '''
  fields = ('iusername', 'timeStampSince', 'timeStampUntil')
  serializer_class = InstagramUserSerializer
  lookup_field = fields

  def get(self, request, iusername, timeStampSince, timeStampUntil):
    user = get_object_or_404(InstagramUser, username=iusername)
    data = request_views_and_followers(user.fbtoken, user.fbid, timeStampSince, timeStampUntil)['data']
    return Response(data, status=HTTP_200_OK)


class InstagramStoryUrls(APIView):
  fields = ('iusername')
  serializer_class = InstagramUserSerializer
  lookup_field = fields

  def get(self, request, iusername):
    user = get_object_or_404(InstagramUser, username=iusername)
    data = request_story_urls(user.fbtoken, user.fbid)
    return Response(data, status=HTTP_200_OK)


class InstagramStoryMetrics(APIView):
  fields = ('iusername')
  serializer_class = InstagramUserSerializer
  lookup_field = fields

  def get(self, request, iusername):
    user = get_object_or_404(InstagramUser, username=iusername)
    data = request_story_stats(user.fbtoken, user.fbid)
    return Response(data, status=HTTP_200_OK)
