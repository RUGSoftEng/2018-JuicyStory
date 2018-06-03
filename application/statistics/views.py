from database.models import InstagramUser
from urllib.parse import urlparse
from django.shortcuts import get_object_or_404, redirect
from .serializers import InstagramUserSerializer

from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.views import APIView


def url_redirect(request, iusername):
  testy = "http://localhost:8000/api/metrics/" + iusername + "/"  #"/get-fb-token/"
  client_id = "687645918026028"
  scope = "ads_management,business_management,manage_pages,pages_show_list,instagram_basic,instagram_manage_insights,read_insights"
  test_url = "https://www.facebook.com/v3.0/dialog/oauth?client_id=" + client_id + "&redirect_uri=" + testy + "&scope=" + scope
  return redirect(test_url)


def get_token(request, iusername):
  user = get_object_or_404(InstagramUser, username=iusername)
  code = urlparse(request.get_full_path()).query[5:]
  testy = "http://localhost:8000/api/metrics/" + iusername + "/"  #"/get-fb-token/"

  token_url = "https://graph.facebook.com/v3.0/oauth/access_token"
  token_data = requests.get(
    token_url,
    params={
      "client_id": "687645918026028",
      "redirect_uri": testy,
      "client_secret": "ca58315c52af459be1f75302f6d5ddc3",
      "code": code
    }).json()
  user.fbtoken = token_data["access_token"]

  #return redirect("http://localhost:8000/" + iusername)


def retrieve_token(request, iusername):
  url_redirect(request, iusername)
  get_token(request, iusername)


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
    #retrieve_token(request, iusername)
    data = get_story_metrics(request, iusername)
    return Response(data, status=HTTP_200_OK)


class InstagramStoryMetrics(APIView):
  fields = ('iusername')
  serializer_class = InstagramUserSerializer
  lookup_field = fields

  def get(self, request, iusername):
    user = get_object_or_404(InstagramUser, username=iusername)
    data = request_story_stats(user.fbtoken, user.fbid)
    return Response(data, status=HTTP_200_OK)
