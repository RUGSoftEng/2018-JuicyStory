import requests
from django.shortcuts import render
from .models import InstagramClient, InstagramUser


def get_access_token(auth_code):
  url = "https://api.instagram.com/oauth/access_token"
  client = InstagramClient.objects.get(pk=1)
  post_data = {'client_id': client.client_id, 'client_secret': client.client_secret,
               'grant_type': 'authorization_code', 'redirect_uri': client.redirect_uri, 'code': auth_code}
  response = requests.post(url, data=post_data)
  content = response.json()
  return content


def process_auth_code(request):
  if 'code' in request.GET:
    code = request.GET['code']
    response = get_access_token(code)
    if "error_type" in response:
      print(response)
    else: 
      access_token = response['access_token']
      username = response['user']['username']
      print(username)

      user = InstagramUser.objects.get(username=username)
      user.access_token = access_token
      user.save()

  return user_list(request)


def user_list(request):
  clients = InstagramClient.objects.values()
  context = {'user': clients[0]}
  return render(request, 'authcode/user_list.html', context)
