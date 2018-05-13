from django.db import models
from django.contrib.auth.models import User

''' The instagram user accounts that we retrieve information '''
class InstagramUser(models.Model):
  username = models.CharField(max_length=30)
  password = models.CharField(max_length=50)
  fbtoken = models.CharField(max_length=300, blank=True)
  fbid = models.CharField(max_length=50, blank = True)
  access_token = models.CharField(max_length=100, blank=True)
  owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

''' The data regarding upcoming image uploads '''
class ScheduledImage(models.Model):
  username = models.CharField(max_length=30)
  image_file = models.ImageField(upload_to='images/%Y/%m/%d')
  upload_date = models.DateTimeField()
  is_story = models.BooleanField()

''' Images that are selected by an instagramUser '''
class SelectedImage(models.Model):
	instagram_user = models.ForeignKey(InstagramUser, default=None, on_delete=models.CASCADE)
	photo = models.CharField(max_length=300)
