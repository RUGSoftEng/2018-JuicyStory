import requests


def request_images_by_tag(tag, access_token):
  url = "https://api.instagram.com/v1/tags/%s/media/recent" % tag
  response = requests.get(
      url, params={'access_token': access_token})
  return response.json()


def get_geography_by_address(address):
  url = "https://maps.google.com/maps/api/geocode/json"
  response = requests.get(url, params={'address': address})
  return response.json()['results'][0]['geometry']['location']


def request_images_by_location(location, access_token):
  search_url = 'https://api.instagram.com/v1/locations/search'
  # try:
  geography = get_geography_by_address(location)
  response = requests.get(search_url, params={
                          'lat': geography['lat'], 'lng': geography['lng'], 'access_token': access_token, 'distance': 500})
  location_id = response.json()['data'][0]['id']
  return (response.json())
  location_url = 'https://api.instagram.com/v1/locations/%s/media/recent' % location_id
  response = requests.get(location_url, params={'access_token': access_token})
  return response.json()

  # except:
  #   return {'error': 'Error while getting the images'}
