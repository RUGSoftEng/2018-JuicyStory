from authentication.models import InstagramUser
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .utils import *
import json


#access token is placeholder for fb user token and insta business id
def somePage(request, iusername):
	user = get_object_or_404(InstagramUser, username=iusername)
	return render(request, "stats/test.html", {'instagram_user':user})

# Gets reach and impressions
def getProfileStats(request,access_token):
	timeframe = request.GET.get('timeframe')
	userData = requestImpressions(access_token,timeframe)
	return HttpResponse(json.dumps(userData))

#gets profile views and follower count
def getViewsAndCount(request,access_token):
	userData = requestViewsAndFollowers(access_token)
	return HttpResponse(json.dumps(userData))

def getLifetime(request,access_token):
	userData = requestLifetimeStats(access_token)
	return HttpResponse(json.dumps(userData))