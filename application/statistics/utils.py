import requests
from incoming.utils import get_self_user_info
import json

def request_impressions(access_token,timeframe,fbId,timeStampSince,timeStampUntil):

	userId = get_id(fbId,access_token)

	url = "https://graph.facebook.com/" + userId +"/insights"
	response = requests.get(url,params={"access_token": access_token,"metric":"impressions,reach","period":timeframe,"since":timeStampSince,"until":timeStampUntil})

	return response.json()

def request_views_and_followers(access_token,fbId,timeStampSince,timeStampUntil):

	userId = get_id(fbId,access_token)

	url = "https://graph.facebook.com/" + userId +"/insights"
	response = requests.get(url,params={"access_token": access_token,"metric":"follower_count,profile_views","period":"day","since":timeStampSince,"until":timeStampUntil})

	return response.json()


def request_lifetime_stats(access_token,fbId,timeStampSince,timeStampUntil):

	userId = get_id(fbId,access_token)

	url = "https://graph.facebook.com/" + userId +"/insights"
	response = requests.get(url,params={"access_token": access_token,"metric":"audience_gender_age,audience_locale,audience_country,audience_city,online_followers","period":"lifetime",
		"since":timeStampSince,"until":timeStampUntil})

	return response.json()

def get_id(fbId,access_token):
	url = "https://graph.facebook.com/" + fbId
	getUser = requests.get(url,params={"access_token": access_token,"fields":"instagram_business_account"})
	userId = getUser.json()["instagram_business_account"]["id"]
	return userId

