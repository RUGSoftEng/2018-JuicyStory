import requests
from incoming.utils import get_self_user_info
import json
#access_token is place holder for fb user token
def requestImpressions(access_token,timeframe):

	#hard coded user token and fb id
	facebook_access_token = "EAACEdEose0cBAKrTeeeiga4TiYhnZAKcbeIwzy6ZBJXiTp1MseyZBkhoK2MzVPr3LjMXhAR95wNtZBX4Vj25ETu8IJa90U2LZA1FbvUmw6veVjLCmx1xZAkmII4pMLTtcpiFmlooxsI1sRyIMisHub5epng8T2qDQH94Q0kpmmFpebZAoriIeixz4WScA8IP68LCjfNNl8UotoEDJIKsrgHuvfItapLFOEZB5vIVWI3dZBFkAZAMUMTPkH58Dkk6OfY04ZD"
	url = "https://graph.facebook.com/" + "160447804650500"

	#this step should be moved to login phase
	getUser = requests.get(url,params={"access_token": facebook_access_token,"fields":"instagram_business_account"})
	userId = getUser.json()["instagram_business_account"]["id"]


	url = "https://graph.facebook.com/" + userId +"/insights"
	response = requests.get(url,params={"access_token": facebook_access_token,"metric":"impressions,reach","period":timeframe})

	return response.json()

def requestViewsAndFollowers(access_token):

	#hard coded user token and fb id
	facebook_access_token = "EAACEdEose0cBAKrTeeeiga4TiYhnZAKcbeIwzy6ZBJXiTp1MseyZBkhoK2MzVPr3LjMXhAR95wNtZBX4Vj25ETu8IJa90U2LZA1FbvUmw6veVjLCmx1xZAkmII4pMLTtcpiFmlooxsI1sRyIMisHub5epng8T2qDQH94Q0kpmmFpebZAoriIeixz4WScA8IP68LCjfNNl8UotoEDJIKsrgHuvfItapLFOEZB5vIVWI3dZBFkAZAMUMTPkH58Dkk6OfY04ZD"
	url = "https://graph.facebook.com/" + "160447804650500"

	#this step should be moved to login phase
	getUser = requests.get(url,params={"access_token": facebook_access_token,"fields":"instagram_business_account"})
	userId = getUser.json()["instagram_business_account"]["id"]

	url = "https://graph.facebook.com/" + userId +"/insights"
	response = requests.get(url,params={"access_token": facebook_access_token,"metric":"follower_count,profile_views","period":"day"})

	return response.json()


def requestLifetimeStats(access_token):
	#hard coded user token and fb id
	facebook_access_token = "EAACEdEose0cBAKrTeeeiga4TiYhnZAKcbeIwzy6ZBJXiTp1MseyZBkhoK2MzVPr3LjMXhAR95wNtZBX4Vj25ETu8IJa90U2LZA1FbvUmw6veVjLCmx1xZAkmII4pMLTtcpiFmlooxsI1sRyIMisHub5epng8T2qDQH94Q0kpmmFpebZAoriIeixz4WScA8IP68LCjfNNl8UotoEDJIKsrgHuvfItapLFOEZB5vIVWI3dZBFkAZAMUMTPkH58Dkk6OfY04ZD"
	url = "https://graph.facebook.com/" + "160447804650500"

	#this step should be moved to login phase
	getUser = requests.get(url,params={"access_token": facebook_access_token,"fields":"instagram_business_account"})
	userId = getUser.json()["instagram_business_account"]["id"]

	url = "https://graph.facebook.com/" + userId +"/insights"
	response = requests.get(url,params={"access_token": facebook_access_token,"metric":"audience_gender_age,audience_locale,audience_country,audience_city,online_followers","period":"lifetime"})

	return response.json()
