
from database.models import InstagramUser
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .utils import *
import json

# Gets reach and impressions
def get_profile_stats(request,iusername,timeFrame,timeStampSince,timeStampUntil):
	user = get_object_or_404(InstagramUser, username=iusername)
	userData = request_impressions(user.fbtoken,user.fbid,timeFrame,timeStampSince,timeStampUntil)

	context = {'userdata': userData, 'instagram_user':user}
	return render(request, "statistics/statistics.html",context)

#gets profile views and follower count
def get_views_and_count(request,iusername,timeStampSince,timeStampUntil):
	user = get_object_or_404(InstagramUser, username=iusername)
	userData = request_views_and_followers(user.fbtoken,user.fbid,timeStampSince,timeStampUntil)
	print(userData)
	context = {'userdata': userData, 'instagram_user':user}
	return render(request, "statistics/statistics.html",context)

def get_lifetime(request,iusername,timeStampSince,timeStampUntil):
	user = get_object_or_404(InstagramUser, username=iusername)
	userData = request_lifetime_stats(user.fbtoken,user.fbid,timeStampSince,timeStampUntil)

	context = {'userdata': userData, 'instagram_user':user}
	return render(request, "statistics/statistics.html",context)