
from database.models import InstagramUser
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .utils import *
from .serializers import InstagramUserSerializer
import json

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter

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

class FilterInstagramUser(APIView):
	''' Api for setting filters based on the field attributes below '''
	serializer_class 	= InstagramUserSerializer
	permission_classes 	= (IsAuthenticated,)

	def get(self, request, iusername, timeStampSince, timeStampUntil):
		data = get_views_and_count(request,iusername,timeStampSince,timeStampUntil)
		return Response(data)


