
from database.models import InstagramUser
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .utils import *
import json

# Gets reach and impressions
def getProfileStats(request,iusername,timeFrame,timeStampSince,timeStampUntil):
	user = get_object_or_404(InstagramUser, username=iusername)
	userData = requestImpressions(user.fbtoken,user.fbid,timeFrame,timeStampSince,timeStampUntil)

	context = {'userdata': userData, 'instagram_user':user}
	return render(request, "statistics/statistics.html",context)

#gets profile views and follower count
def getViewsAndCount(request,iusername,timeStampSince,timeStampUntil):
	user = get_object_or_404(InstagramUser, username=iusername)
	userData = requestViewsAndFollowers(user.fbtoken,user.fbid,timeStampSince,timeStampUntil)
	print(userData)
	context = {'userdata': userData, 'instagram_user':user}
	return render(request, "statistics/statistics.html",context)

def getLifetime(request,iusername,timeStampSince,timeStampUntil):
	user = get_object_or_404(InstagramUser, username=iusername)
	userData = requestLifetimeStats(user.fbtoken,user.fbid,timeStampSince,timeStampUntil)

	context = {'userdata': userData, 'instagram_user':user}
	return render(request, "statistics/statistics.html",context)