from django.shortcuts import render, get_object_or_404, redirect
from instagramAPI.utils import InstagramAPI
from database.models import InstagramUser, SelectedImage
from .utils import get_self_user_info, request_images_by_tag, request_images_by_location_id, query_locations_by_name

def list_images(request, iusername):
  user = get_object_or_404(InstagramUser, username=iusername)
  access_token = user.access_token
  userdata = get_self_user_info(access_token)

  # got an error, try to acquire a new access token
  if "data" not in userdata:
    return redirect('authcode:get_code')    

  userdata = userdata["data"]
  # images from the request
  images = {}
  places = {}

  if 'tag_or_location' in request.GET:
    if request.GET['tag_or_location'][0] == '#':
      tag = request.GET['tag_or_location'][1:]
      images = request_images_by_tag(tag, access_token)
    else:
      location = request.GET['tag_or_location']
      places = query_locations_by_name(location)
  elif 'id' in request.GET:
    images = request_images_by_location_id(request.GET['id'], access_token)

  print(images)

  context = {
  'userdata': userdata,
  'images': images,
  'places':places,
  'instagram_user':user}

  return render(request, 'incoming/incoming_images.html', context)

def list_dm_images(request, iusername):
  user = get_object_or_404(InstagramUser, username=iusername)
  access_token = user.access_token
  userdata = get_self_user_info(access_token)
  print(userdata)

  # got an error, try to acquire a new access token
  if "data" not in userdata:
    return redirect('authentication:get_code')

  # Get the DMs
  instagram_api = InstagramAPI(user)
  instagram_api.login()
  instagram_api.get_v2_inbox()

  DMResponse = instagram_api.last_json
  userdata = userdata["data"]
  print(userdata)
  images = {}
  places = {}
  DMImages = {}

  for messageThread in DMResponse['inbox']['threads']:
    for item in messageThread['items']:
      if 'media' in item:
        DMImages[item['timestamp']] = item['media']['image_versions2']['candidates'][0]['url']
  orderedDMTimestamps = sorted(DMImages.keys())

  if 'tag_or_location' in request.GET:
    if request.GET['tag_or_location'][0] == '#':
      tag = request.GET['tag_or_location'][1:]
      images = request_images_by_tag(tag, access_token)
    else:
      location = request.GET['tag_or_location']
      places = query_locations_by_name(location)

  elif 'id' in request.GET:
    images = request_images_by_location_id(request.GET['id'], access_token)

  context = {
    'userdata': userdata,
    'images': images,
    'places': places,
    'DMImages': DMImages,
    'orderedDMTimestamps': orderedDMTimestamps,
    'instagram_user': user
  }
  return render(request, 'incoming/incoming_images.html', context)


# Select an image and save it in the databse
def select_images(request, iusername):
  user = get_object_or_404(InstagramUser, username=iusername)
  image_url = request.POST.getlist('url')
  for url in image_url:
    if url:
      SelectedImage.objects.create(instagram_user=user, photo=url)
  return redirect('upload:list_selected_images', iusername)
