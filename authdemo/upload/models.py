from django.db import models


class Image(models.Model):
  username = models.CharField(max_length=30)
  image_file = models.FileField(upload_to='images/%Y/%m/%d')
  upload_date = models.DateField()
