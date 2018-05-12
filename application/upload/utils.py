import time
import requests.sessions
from urllib import request
from urllib.parse import urlparse
from database.models import SelectedImage, Image, InstagramUser
from datetime import datetime
from django.core.files.images import ImageFile
from instagramAPI.utils import InstagramAPI
from django.core.exceptions import ObjectDoesNotExist

def upload_image(username, photo):
    instagram_api = InstagramAPI("testy8101", "%3zf(^u7YX")
    instagram_api.login()
    instagram_api.uploadPhoto(photo)


def upload_story(iusername, photo):
    try:
      user = InstagramUser.objects.get(username=iusername)
    except ObjectDoesNotExist:
      return 

    instagram_api = InstagramAPI(user.username, user.password)
    instagram_api.login()
    instagram_api.uploadStoryPhoto(photo)


def parseDateTime(date, time):
    date = date.split('-')
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])

    time = time.split(':')
    hour = int(time[0])
    minute = int(time[1])

    return datetime(year, month, day, hour, minute)


def download_schedule_image(image_url, iusername, date, time):
    response = requests.get(image_url, stream=True)

    if response.status_code != requests.codes.ok:
        return

    result = request.urlretrieve(image_url)
    image_file = ImageFile(open(result[0], 'rb'))

    image = Image()
    image.username = iusername
    image.is_story = True
    image.upload_date = parseDateTime(date, time)
    image.image_file.save(urlparse(image_url).path.split(
        '/')[-1], image_file, save=True)

    SelectedImage.objects.filter(photo=image_url).delete()
