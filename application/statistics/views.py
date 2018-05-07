
from database.models import InstagramUser
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .utils import *
import json

# Gets reach and impressions
def getProfileStats(request,iusername,timeframe):
	user = get_object_or_404(InstagramUser, username=iusername)
	userData = requestImpressions(user.fbtoken,user.fbid,timeframe)

	context = {'userdata': userData, 'instagram_user':user}
	return render(request, "statistics/statistics.html",context)

#gets profile views and follower count
def getViewsAndCount(request,iusername):
	user = get_object_or_404(InstagramUser, username=iusername)
	userData = requestViewsAndFollowers(user.fbtoken,user.fbid)

	context = {'userdata': userData, 'instagram_user':user}
	return render(request, "statistics/statistics.html",context)

def getLifetime(request,iusername):
	user = get_object_or_404(InstagramUser, username=iusername)
	userData = requestLifetimeStats(user.fbtoken,user.fbid)

	context = {'userdata': userData, 'instagram_user':user}
	return render(request, "statistics/statistics.html",context)