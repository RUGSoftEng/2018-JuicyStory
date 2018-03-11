from django.shortcuts import render, get_object_or_404
from authcode.models import InstagramUser
from django.http import JsonResponse
from .utils import request_images_by_tag, request_images_by_location, get_self_user_info


def list_images(request, username):
  user = get_object_or_404(InstagramUser, username=username)
  access_token = user.access_token
  userdata = get_self_user_info(access_token)["data"]
  images = {}

  if 'tag_or_location' in request.GET:
    if request.GET['tag_or_location'][0] == '#':
      tag = request.GET['tag_or_location'][1:]
      images = request_images_by_tag(tag, access_token)['data']
    else:
      pass
      # location = request.GET['tag_or_location']
      # images = request_images_by_location(location, access_token)

    # return JsonResponse(images)

  return render(request, 'location/list_images.html', {'userdata': userdata, 'images': images})
