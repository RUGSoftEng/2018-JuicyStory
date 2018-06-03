
from database.models import InstagramUser
from django.utils import timezone
from urllib.parse import urlparse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .utils import *
from .serializers import InstagramUserSerializer
import json

from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST)
from rest_framework.response import Response
from rest_framework.views import APIView

# Gets reach and impressions
def get_profile_stats(request,iusername,timeFrame,timeStampSince,timeStampUntil):
	user = get_object_or_404(InstagramUser, username=iusername)
	userData = request_impressions(user.fbtoken,user.fbid,timeFrame,timeStampSince,timeStampUntil)

	context = {'userdata': userData, 'instagram_user':user}
	return render(request, "statistics/statistics.html",context)

#gets profile views and follower count
def get_views_and_count(request,iusername,timeStampSince,timeStampUntil):
	user = get_object_or_404(InstagramUser, username=iusername)
	#timeStampSince = 1526109291
	#timeStampUntil = 1526413193
	userData = request_views_and_followers(user.fbtoken,user.fbid,timeStampSince,timeStampUntil)
	userData = userData['data']
	return userData

def get_lifetime(request,iusername,timeStampSince,timeStampUntil):
	user = get_object_or_404(InstagramUser, username=iusername)
	userData = request_lifetime_stats(user.fbtoken,user.fbid,timeStampSince,timeStampUntil)

	context = {'userdata': userData, 'instagram_user':user}
	return render(request, "statistics/statistics.html",context)

def get_story_metrics(request, iusername):
	user = get_object_or_404(InstagramUser, username=iusername)
	return request_story_stats(user.fbtoken,user.fbid)

def get_story_urls(request, iusername):
	user = get_object_or_404(InstagramUser, username=iusername)
	return request_story_urls(user.fbtoken,user.fbid)

def url_redirect(request, iusername):
	testy = "http://localhost:8000/api/metrics/" + iusername + "/"#"/get-fb-token/"
	client_id = "687645918026028"
	scope = "ads_management,business_management,manage_pages,pages_show_list,instagram_basic,instagram_manage_insights,read_insights"
	test_url = "https://www.facebook.com/v3.0/dialog/oauth?client_id=" + client_id + "&redirect_uri=" + testy + "&scope=" + scope
	return redirect(test_url)

def get_token(request, iusername):
	user = get_object_or_404(InstagramUser, username=iusername)
	code = urlparse(request.get_full_path()).query[5:]
	testy = "http://localhost:8000/api/metrics/" + iusername + "/"#"/get-fb-token/"

	token_url = "https://graph.facebook.com/v3.0/oauth/access_token"
	token_data = requests.get(token_url,params={
		"client_id":"687645918026028",
		"redirect_uri":testy,
		"client_secret":"ca58315c52af459be1f75302f6d5ddc3",
		"code":code}).json()
	user.fbtoken = token_data["access_token"]

	#return redirect("http://localhost:8000/" + iusername)

def retrieve_token(request, iusername):
	url_redirect(request, iusername)
	get_token(request, iusername)

class FilterInstagramUserStatistics(APIView):
	''' Api for setting filters based on the field attributes below '''
	fields 				= ('iusername', 'timeStampSince', 'timeStampUntil')
	serializer_class 	= InstagramUserSerializer
	lookup_field 		= fields

	def get(self, request, iusername, timeStampSince, timeStampUntil):
		data = get_views_and_count(request, iusername, timeStampSince, timeStampUntil)
		return Response(data, status=HTTP_200_OK)

class InstagramStoryUrls(APIView):
	fields 				= ('iusername')
	serializer_class	= InstagramUserSerializer
	lookup_field		= fields

	def get(self, request, iusername):
		data = get_story_urls(request, iusername)
		return Response(data, status=HTTP_200_OK)

class InstagramStoryMetrics(APIView):
	fields 				= ('iusername')
	serializer_class	= InstagramUserSerializer
	lookup_field		= fields

	def get(self, request, iusername):
		#retrieve_token(request, iusername)
		data = get_story_metrics(request, iusername)
		return Response(data, status=HTTP_200_OK)


