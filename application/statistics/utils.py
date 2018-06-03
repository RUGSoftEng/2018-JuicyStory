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

def request_story_urls(access_token,fbId):
	userId = get_id(fbId,access_token)

	storyUrl = "https://graph.facebook.com/" + userId + "/stories"

	storyResponse = requests.get(storyUrl,params={"access_token":access_token})
	mediaIds = storyResponse.json()["data"]

	urls = []

	for mediaId in mediaIds:

		graphUrl = "https://graph.facebook.com/" + mediaId["id"]
		mediaData = requests.get(graphUrl,params={"access_token": access_token, "fields":"media_url"})
		data = mediaData.json()

		if(next(iter(data)) != "error"):
			urls.append(data["media_url"])

	return urls
		

def request_story_stats(access_token,fbId):
	userId = get_id(fbId,access_token)

	storyUrl = "https://graph.facebook.com/" + userId + "/stories"

	storyResponse = requests.get(storyUrl,params={"access_token":access_token})
	mediaIds = storyResponse.json()["data"]
	result = {"exits":0,"impressions":0,"reach":0,"replies":0,"taps_forward":0,"taps_back":0}

	for mediaId in mediaIds:
		
		metricUrl = "https://graph.facebook.com/" + mediaId["id"] + "/insights"
		mediaResponse = requests.get(metricUrl,params={"access_token": access_token,"metric":"exits,impressions,reach,replies,reach,taps_forward,taps_back"})
		getData = mediaResponse.json()

		print(getData)
		if(next(iter(getData)) != "error"):
			result["exits"] = result["exits"] + getData["data"][0]["values"][0]["value"]
			result["impressions"] = result["impressions"] + getData["data"][1]["values"][0]["value"]
			result["reach"] = result["reach"] + getData["data"][2]["values"][0]["value"]
			result["replies"] = result["replies"] + getData["data"][3]["values"][0]["value"]
			result["taps_forward"] = result["taps_forward"] + getData["data"][4]["values"][0]["value"]
			result["taps_back"] = result["taps_back"] + getData["data"][5]["values"][0]["value"]
			
	return result


def get_id(fbId,access_token):
	url = "https://graph.facebook.com/" + fbId
	getUser = requests.get(url,params={"access_token": access_token,"fields":"instagram_business_account"})
	userId = getUser.json()["instagram_business_account"]["id"]
	return userId

