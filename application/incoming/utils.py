import requests
from django.core.exceptions import ObjectDoesNotExist
from instagramAPI.utils import InstagramAPI
from database.models import InstagramUser


def get_self_user_info(access_token):
  ''' Gets information based on the retrieved access_token such as,
  username, profile_picture, full_name, bio, is_business etc
  '''
  url = "https://api.instagram.com/v1/users/self/"
  response = requests.get(url, params={"access_token": access_token})
  return response.json()


def request_images_by_tag(tag, access_token):
  """ Queries the instagram API for images with the given tag.
    Strips the response and returns a dict : {timestamp : image url}
  """
  result_images = {}
  url = "https://api.instagram.com/v1/tags/%s/media/recent" % tag
  response = requests.get(url, params={"access_token": access_token})

  for image in response.json()["data"]:
    result_images[image["caption"]["created_time"]] = image["images"]["standard_resolution"]["url"]

  return result_images


def query_locations_by_name(location_name):
  """ Queries the facebook graph API for places with the given name. """
  facebook_access_token = "193757027889836|y0gKhLCNcHx-Yah6FCLiT823RNc"
  url = "https://graph.facebook.com/search"

  response = requests.get(url, params={"access_token": facebook_access_token, "q": location_name, "type": "place"})

  return response.json()


def convert_facebook_id_to_insta_id(facebook_places_id, access_token):
  """ Converts a facebook places ID to Instagram location ID by querying
    the instagram API.
  """
  search_url = 'https://api.instagram.com/v1/locations/search'
  response = requests.get(search_url, params={"facebook_places_id": facebook_places_id, 'access_token': access_token})
  return response.json()['data'][0]['id']


def request_images_by_location_id(facebook_places_id, access_token):
  """ Queries the instagram API for images for a certain place.
    Place should be passed as a facebook places id.
  """
  insta_id = convert_facebook_id_to_insta_id(facebook_places_id, access_token)
  url = 'https://api.instagram.com/v1/locations/%s/media/recent' % insta_id
  response = requests.get(url, params={'access_token': access_token})
  return response.json()['data']


def get_DM_Images(user):
  """ Acquires the inbox for the user and strips the images.
    The output is formatted as a dict that is {timestamp: image url}
  """
  DM_images = {}

  instagram_api = InstagramAPI(user)
  instagram_api.login()
  instagram_api.get_v2_inbox()
  DMResponse = instagram_api.last_json

  if ("error" in DMResponse):
    return DMResponse

  for messageThread in DMResponse['inbox']['threads']:
    for item in messageThread['items']:
      if 'media' in item:
        DM_images[item['timestamp']] = item['media']['image_versions2']['candidates'][0]['url']

  return DM_images


def list_images(iusername, tag=None, location_id=None, get_DM=None):
  """  Returns a dictionary of images with the given tag/location_id 
    and also images from the DMs if requested. 

    In return dict, timestamps of posted images are the keys and the 
    image URLs are the values.
    """
  all_images = {}

  try:
    user = InstagramUser.objects.get(username=iusername)
  except ObjectDoesNotExist:
    return {"error": "No instagram user with that username found."}

  access_token = user.access_token

  try:
    if tag:
      tag_images = request_images_by_tag(tag, access_token)
      all_images.update(tag_images)

    if location_id:
      location_images = request_images_by_location_id(location_id, access_token)
      all_images.update(location_images)

    if get_DM:
      DM_images = get_DM_Images(user)
      all_images.update(DM_images)
  except Exception as e:
    print(str(e))
    #return {"error": "An undetermined error occured while requesting images."}

  return all_images


def validate_ownership(user, instagram_username):
  """ Returns true if the given user owns the given instagram account """
  try:
    instagram_user = InstagramUser.objects.get(username=instagram_username)
  except ObjectDoesNotExist:
    return {"error": "No instagram user with that username found."}

  return instagram_user.owner == user
