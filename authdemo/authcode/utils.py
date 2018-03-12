import requests
from .models import InstagramClient

def get_access_token(auth_code):
  url = "https://api.instagram.com/oauth/access_token"
  client = InstagramClient.objects.get(pk=1)
  post_data = {'client_id': client.client_id, 'client_secret': client.client_secret,
               'grant_type': 'authorization_code', 'redirect_uri': client.redirect_uri, 'code': auth_code}
  response = requests.post(url, data=post_data)
  content = response.json()
  return content

