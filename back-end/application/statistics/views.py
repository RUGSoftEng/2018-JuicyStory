from database.models import InstagramUser
from urllib.parse import urlparse
from django.shortcuts import get_object_or_404, redirect
from .serializers import InstagramUserSerializer
from .utils import (request_views_and_followers, request_story_stats, request_story_urls)

from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
#Obsolete method when using html, kept for debugging
def get_story_metrics(request,iusername):
  user = get_object_or_404(InstagramUser, username=iusername)
  return request_story_stats(user.fbtoken,user.Fbpageid)
#Obsolete method when using html, kept for debugging
def get_views_and_count(request,iusername,timeStampSince,timeStampUntil):
  user = get_object_or_404(InstagramUser, username=iusername)
  #timeStampSince = 1526109291
  #timeStampUntil = 1526413193
  userData = request_views_and_followers(user.fbtoken,user.Fbpageid,timeStampSince,timeStampUntil)
  userData = userData['data']
  return userData

def get_story_urls(request,iusername):
  user = get_object_or_404(InstagramUser, username=iusername)
  return request_story_urls(user.fbtoken,user.fbid)

#This method is called when a token needs to be retrieved from facebook
#After this method is called the user will be redirected to facebook where to accept or deny permissions
#From there facebook will redirect back to our app with a code in the url which is used to retrieve the token, via
# a get request
def fbtoken_redirect(request, iusername):
  '''We set up the redirect url that is going to call the next function attached to it.'''
  testy = "http://localhost:8000/statistics/testy8101/get-fbtoken/"
  client_id = "687645918026028"
  scope = "ads_management,business_management,manage_pages,pages_show_list,instagram_basic,instagram_manage_insights,read_insights"
  test_url = "https://www.facebook.com/v3.0/dialog/oauth?client_id=" + client_id + "&redirect_uri=" + testy + "&scope=" + scope
  return redirect(test_url)

#Gets token and then saves the token and facebook id
def get_token(request, iusername):
  user = get_object_or_404(InstagramUser, username=iusername)
  code = urlparse(request.get_full_path()).query[5:]
  testy = "http://localhost:8000/statistics/testy8101/get-fbtoken/"
  print(request.get_full_path())
  token_url = "https://graph.facebook.com/v3.0/oauth/access_token"
  token_data = requests.get(token_url,
    params={
      "client_id": "687645918026028",
      "redirect_uri": testy,
      "client_secret": "ca58315c52af459be1f75302f6d5ddc3",
      "code": code
    }).json()
  user.fbtoken = token_data["access_token"]

  id_url = "https://graph.facebook.com/me"

  id_data = requests.get(id_url,params={"access_token":user.fbtoken}).json()
  user.fbid = id_data["id"]
  user.save()


#Page id is used to get the business account of a user, thus we use a get request to store it in our database
def getPageId(request, iusername, page_name):
  user = get_object_or_404(InstagramUser, username=iusername)
  get_url = "https://graph.facebook.com/" + user.fbid + "/accounts"

  page_data = requests.get(get_url,params={"access_token":user.fbtoken}).json()
  user.fbpageid = page_data['data'][0]['id']
  user.save()



class FilterInstagramUserStatistics(APIView):
  ''' Api for setting filters based on the field attributes below '''
  fields = ('iusername', 'timeStampSince', 'timeStampUntil')
  serializer_class = InstagramUserSerializer
  lookup_field = fields

  def get(self, request, iusername, timeStampSince, timeStampUntil):
    #user = get_object_or_404(InstagramUser, username=iusername)
    data = get_views_and_count(request, iusername, timeStampSince, timeStampUntil)
    return Response(data, status=HTTP_200_OK)


class InstagramStoryUrls(APIView):
  fields = ('iusername')
  serializer_class = InstagramUserSerializer
  lookup_field = fields

  def get(self, request, iusername):
    data = get_story_urls(request, iusername)
    return Response(data, status=HTTP_200_OK)


class InstagramStoryMetrics(APIView):
  fields = ('iusername')
  serializer_class = InstagramUserSerializer
  lookup_field = fields

  def get(self, request, iusername):
    user = get_object_or_404(InstagramUser, username=iusername)
    data = request_story_stats(user.fbtoken, user.fbpageid)
    return Response(data, status=HTTP_200_OK)
