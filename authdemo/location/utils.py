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


def request_ids_by_coordinate(coordinates, access_token):
  search_url = 'https://api.instagram.com/v1/locations/search'
  response = requests.get(search_url, params={
                          'lat': coordinates['lat'], 'lng': coordinates['lng'], 'access_token': access_token, 'distance': 500})
  return response.json()['data'][:5]

def request_images_by_location_id(location_id, access_token):
  url = 'https://api.instagram.com/v1/locations/%s/media/recent' % location_id
  response = requests.get(url, params={'access_token': access_token})
  return response.json()['data']
