import requests

# TODO: HIDE THE SECRET!
def get_client_info():
  ''' Store the information in the database '''
  return {
      "client_id": "a81a42fcf5eb4194b4905822fc05f56a",
      "redirect_uri": "http://80.114.178.251/auth/receive_code",
      "client_secret": "0d2e5ce1664b477d8aca11201b5dd779"}

def get_access_token(auth_code):
  ''' Get the access token using the instagram
  information above '''
  client    = get_client_info()
  post_data = {
      'client_id': client["client_id"],
      'client_secret': client["client_secret"],
      'grant_type': 'authorization_code',
      'redirect_uri': client["redirect_uri"],
      'code': auth_code}
  url       = "https://api.instagram.com/oauth/access_token"
  response  = requests.post(url, data=post_data)
  content   = response.json()
  return content
