from django_cron import CronJobBase, Schedule
from .models import Image
from .utils import upload_image
import datetime
from django.conf import settings


class ImageUploadCronJob(CronJobBase):
  RUN_EVERY_MINS = 1
  RETRY_AFTER_FAILURE_MINS = 1

  schedule = Schedule(run_every_mins=RUN_EVERY_MINS,
                      retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
  code = 'upload.ImageUploadCronJob'

  def do(self):
    images = Image.objects.filter(upload_date__lte=datetime.datetime.now())

    for image in images:    
      try:
        upload_image(image.username, settings.BASE_DIR +
                     '/' + image.image_file.url, True)
        image.delete()
      except Exception as e:
        print(e)
