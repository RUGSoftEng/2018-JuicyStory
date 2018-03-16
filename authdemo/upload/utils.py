import time
import requests.sessions

def upload_image(user, photo):
  with requests.Session() as s:
    baseurl = "https://www.instagram.com/"
    loginurl = baseurl + "accounts/login/ajax/"
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"
    data = {"username": "testy8101", "password": "%3zf(^u7YX"}

    s.headers = {'User-Agent': USER_AGENT}
    s.headers.update({'Referer': baseurl})

    # get the cookies by going to the base site
    r = s.get(baseurl)
    s.headers.update({'X-CSRFToken': r.cookies['csrftoken']})

    # login
    r = s.post(loginurl, data=data, allow_redirects=True)
    s.headers.update({'X-CSRFToken': r.cookies['csrftoken']})

    #######

    # upload the image
    uploadurl = baseurl + "create/upload/photo/"
    s.headers.update({'Referer': baseurl + 'create/style/'})
    upload_id = str(int(time.time() * 1000))
    path = "1991-11.jpg"

    data = {'upload_id': upload_id}
    files = {'photo': open(path, 'rb')}
    s.post(uploadurl, data, files=files)

    # post it
    posturl = baseurl + "create/configure/"
    s.post(posturl, data=data)