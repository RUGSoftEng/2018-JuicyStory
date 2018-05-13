import requests.sessions
from urllib import request
from urllib.parse import urlparse
from database.models import SelectedImage, Image, InstagramUser
from datetime import datetime
from django.core.files.images import ImageFile
from instagramAPI.utils import InstagramAPI
from django.core.exceptions import ObjectDoesNotExist


def upload_image(iusername, photo):
    """ Upload the given image as a post for the given instagram user """
    try:
        user = InstagramUser.objects.get(username=iusername)
    except ObjectDoesNotExist:
        return

    instagram_api = InstagramAPI(user)
    instagram_api.login()
    instagram_api.upload_photo(photo)


def upload_story(iusername, photo):
    """ Upload the given image as a story for the given instagram user """
    try:
        user = InstagramUser.objects.get(username=iusername)
    except ObjectDoesNotExist:
        return

    instagram_api = InstagramAPI(user)
    instagram_api.login()
    instagram_api.upload_story_photo(photo)


def parseDateTime(date, time="00:00"):
    """ Parses the given date and time strings into a python datetime object.
    Expected format is YEAR-MONTH-DAY for the year and HOUR:MINUTE for the time.
    """ 
    date = date.split('-')
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])

    time = time.split(':')
    hour = int(time[0])
    minute = int(time[1])

    return datetime(year, month, day, hour, minute)


def download_and_schedule_image(image_url, iusername, date, time, is_story=False):
    """ Download the given image url and schedule it for upload for the given instagram 
    user with given date and time. 
    """
    response = requests.get(image_url, stream=True)

    if response.status_code != requests.codes.ok:
        return

    result = request.urlretrieve(image_url)
    image_file = ImageFile(open(result[0], 'rb'))

    image = Image()
    image.username = iusername
    image.is_story = is_story
    image.upload_date = parseDateTime(date, time)
    image.image_file.save(urlparse(image_url).path.split(
        '/')[-1], image_file, save=True)

    SelectedImage.objects.filter(photo=image_url).delete()
