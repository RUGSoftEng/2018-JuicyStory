from django.db import models


class Image(models.Model):
  username = models.CharField(max_length=30)
  image_file = models.ImageField(upload_to='images/%Y/%m/%d')
  upload_date = models.DateTimeField()
  is_story = models.BooleanField()
