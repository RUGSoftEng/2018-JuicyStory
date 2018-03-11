from django.shortcuts import render, get_object_or_404
from authcode.models import InstagramUser
# from django.http import JsonResponse
from .utils import *


def list_images(request, username):
  user = get_object_or_404(InstagramUser, username=username)
  access_token = user.access_token
  userdata = get_self_user_info(access_token)["data"]
  images = {}
  places = {}

  if 'tag_or_location' in request.GET:
    if request.GET['tag_or_location'][0] == '#':
      tag = request.GET['tag_or_location'][1:]
      images = request_images_by_tag(tag, access_token)['data']
    else:
      location = {"lat": "53.2383152", "lng": "6.5349696"} # TODO: Don't hardcode
      places = request_ids_by_coordinate(location, access_token)

  elif 'id' in request.GET:
    images = request_images_by_location_id(request.GET['id'], access_token)

  return render(request, 'image_board/list_images.html', {'userdata': userdata, 'images': images, 'places':places})
