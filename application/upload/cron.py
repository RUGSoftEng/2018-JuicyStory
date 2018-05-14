from django_cron import CronJobBase, Schedule
from database.models import Image
from .utils import upload_image, upload_story
import datetime
from django.conf import settings


class ImageUploadCronJob(CronJobBase):
  RUN_EVERY_MINS = 1
  RETRY_AFTER_FAILURE_MINS = 1

  schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
  code = 'upload.ImageUploadCronJob'

  def do(self):
    images = Image.objects.filter(upload_date__lte=datetime.datetime.now())

    for image in images:
      image_path = settings.BASE_DIR + '/' + image.image_file.url
      try:
        if (image.is_story):
          upload_story(image.username, image_path)
        else:
          upload_image(image.username, image_path)
        image.delete()
      except Exception as e:
        print(e)
