import time
import requests.sessions
import random


def upload_image(username, photo, is_story=None):
  with requests.Session() as s:
    base_url = "https://www.instagram.com/"
    login_url = base_url + "accounts/login/ajax/"
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"
    login_data = {"username": "testy8101", "password": "%3zf(^u7YX"}

    s.headers = {'User-Agent': USER_AGENT}
    s.headers.update({'Referer': base_url})

    # get the cookies by going to the base site
    r = s.get(base_url)
    s.headers.update({'X-CSRFToken': r.cookies['csrftoken']})

    # login
    r = s.post(login_url, data=login_data, allow_redirects=True)
    s.headers.update({'X-CSRFToken': r.cookies['csrftoken']})

    # upload the image
    upload_url = base_url + "create/upload/photo/"
    s.headers.update({'Referer': base_url + 'create/style/'})
    upload_id = str(int(time.time() * 1000))

    data = {'upload_id': upload_id}
    files = {'photo': open(photo, 'rb')}
    s.post(upload_url, data, files=files)

    # post it
    if(is_story):
      data.update({
          'client_shared_at': str(int(time.time())),
          'source_type': 3,
          'configure_mode': 1,
          'client_timestamp': str(int(time.time()) - random.randint(3, 10)),
          'upload_id': upload_id,
      })
      posturl = base_url + "create/configure_to_story/"
    else:
      posturl = base_url + "create/configure/"
    
    s.post(posturl, data=data)
