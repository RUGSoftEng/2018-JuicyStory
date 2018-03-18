from django_cron import CronJobBase, Schedule
from .models import Image
import datetime


class MyCronJob(CronJobBase):
  RUN_EVERY_MINS = 1

  schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
  code = 'upload.my_cron_job'

  def do(self):
    Image.objects.filter(upload_date__lte=datetime.datetime.now()).delete()
