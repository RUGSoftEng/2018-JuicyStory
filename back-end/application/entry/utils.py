import requests


def get_jwt_token(username, password):
  post_data = {'username': username, 'password': password}
  url = 'http://localhost:8000/api/get-token/'
  response = requests.post(url, data=post_data)
  content = response.json()
  return content['token']
