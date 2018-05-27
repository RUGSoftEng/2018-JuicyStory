
from database.models import InstagramUser
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
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

class FilterInstagramUser(APIView):
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
		data = get_story_metrics(request, iusername)
		return Response(data, status=HTTP_200_OK)


