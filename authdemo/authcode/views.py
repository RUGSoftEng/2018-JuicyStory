from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils.http import urlencode
from .models import InstagramUser
from .utils import *


def process_auth_code(request):
  if 'code' in request.GET:
    auth_code = request.GET['code']
    response = get_access_token(auth_code)
    if "error_type" not in response:
      access_token = response['access_token']
      username = response['user']['username']
      user = InstagramUser.objects.get(username=username)
      user.access_token = access_token
      user.save()

  return redirect("image_board:list_images", username)


def user_list(request):
  users = InstagramUser.objects.values()
  context = {'users': users}
  return render(request, 'authcode/user_list.html', context)


def get_code(request):
  client = get_client_info()

  url = "https://api.instagram.com/oauth/authorize/"
  params = {"client_id": client["client_id"], "redirect_uri": client["redirect_uri"],
            "response_type": "code", "scope": "public_content"}
  return HttpResponseRedirect(url + "?" + urlencode(params))
