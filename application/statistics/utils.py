import requests
from incoming.utils import get_self_user_info
import json

def requestImpressions(access_token,timeframe,fbId,timeStampSince,timeStampUntil):

	userId = getId(fbId,access_token)

	url = "https://graph.facebook.com/" + userId +"/insights"
	response = requests.get(url,params={"access_token": access_token,"metric":"impressions,reach","period":timeframe,"since":timeStampSince,"until":timeStampUntil})

	return response.json()

def requestViewsAndFollowers(access_token,fbId,timeStampSince,timeStampUntil):

	userId = getId(fbId,access_token)

	url = "https://graph.facebook.com/" + userId +"/insights"
	response = requests.get(url,params={"access_token": access_token,"metric":"follower_count,profile_views","period":"day","since":timeStampSince,"until":timeStampUntil})

	return response.json()


def requestLifetimeStats(access_token,fbId,timeStampSince,timeStampUntil):

	userId = getId(fbId,access_token)

	url = "https://graph.facebook.com/" + userId +"/insights"
	response = requests.get(url,params={"access_token": access_token,"metric":"audience_gender_age,audience_locale,audience_country,audience_city,online_followers","period":"lifetime",
		"since":timeStampSince,"until":timeStampUntil})

	return response.json()

def getId(fbId,access_token):
	url = "https://graph.facebook.com/" + fbId
	getUser = requests.get(url,params={"access_token": access_token,"fields":"instagram_business_account"})
	userId = getUser.json()["instagram_business_account"]["id"]
	return userId

