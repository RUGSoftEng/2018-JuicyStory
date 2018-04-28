import requests


def get_self_user_info(access_token):
  url = "https://api.instagram.com/v1/users/self/"
  response = requests.get(url, params={"access_token": access_token})
  return response.json()


def request_images_by_tag(tag, access_token):
  url = "https://api.instagram.com/v1/tags/%s/media/recent" % tag
  response = requests.get(
      url, params={'access_token': access_token})
  return response.json()


def query_locations_by_name(location_name):
  facebook_access_token = "193757027889836|y0gKhLCNcHx-Yah6FCLiT823RNc"
  url = "https://graph.facebook.com/search"

  response = requests.get(
      url, params={"access_token": facebook_access_token, "q": location_name, "type": "place"})

  return response.json()["data"][:10]


def convert_facebook_id_to_insta_id(facebook_places_id, access_token):
  search_url = 'https://api.instagram.com/v1/locations/search'
  response = requests.get(search_url, params={
                          "facebook_places_id": facebook_places_id, 'access_token': access_token})
  return response.json()['data'][0]['id']


def request_images_by_location_id(facebook_places_id, access_token):
  insta_id  = convert_facebook_id_to_insta_id(facebook_places_id, access_token)
  url = 'https://api.instagram.com/v1/locations/%s/media/recent' % insta_id
  response = requests.get(url, params={'access_token': access_token})
  return response.json()['data']
