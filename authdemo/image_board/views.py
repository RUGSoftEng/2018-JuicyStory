from django.shortcuts import render, get_object_or_404, redirect
from authcode.models import InstagramUser
from .utils import *


def list_images(request, username):
  user = get_object_or_404(InstagramUser, username=username)
  access_token = user.access_token
  userdata = get_self_user_info(access_token)

  # got an error, try to acquire a new access token
  if "data" not in userdata:
    return redirect('authcode:get_code')    

  userdata = userdata["data"]
  images = {}
  places = {}

  if 'tag_or_location' in request.GET:
    if request.GET['tag_or_location'][0] == '#':
      tag = request.GET['tag_or_location'][1:]
      images = request_images_by_tag(tag, access_token)['data']
    else:
      location = request.GET['tag_or_location']
      places = query_locations_by_name(location)

  elif 'id' in request.GET:
    images = request_images_by_location_id(request.GET['id'], access_token)

  context = {'userdata': userdata, 'images': images, 'places':places}
  return render(request, 'image_board/list_images.html', context)
