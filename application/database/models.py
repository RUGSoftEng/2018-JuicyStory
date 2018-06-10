from picklefield.fields import PickledObjectField
from django.db import models
from django.contrib.auth.models import User


class InstagramUser(models.Model):
  """ The instagram user accounts """
  username      = models.CharField(max_length=30)
  password      = models.CharField(max_length=50)
  fbtoken       = models.CharField(max_length=300, blank=True)
  fbid          = models.CharField(max_length=50, blank=True)
  access_token  = models.CharField(max_length=100, blank=True)
  owner         = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
  # Fields below are intended for persistent logins
  login_session = PickledObjectField(default=None, null=True, blank=True)
  username_id   = PickledObjectField(default=None, null=True, blank=True)


class ScheduledImage(models.Model):
  """ Image scheduled for upload """
  username    = models.CharField(max_length=30)
  image_file  = models.ImageField(upload_to='images/%Y/%m/%d')
  upload_date = models.DateTimeField()
  is_story    = models.BooleanField()


class SelectedImage(models.Model):
  """ Images that are selected by an instagramUser to later be scheduled for upload """
  instagram_user  = models.ForeignKey(InstagramUser, default=None, on_delete=models.CASCADE)
  photo           = models.CharField(max_length=300)

  def serialize(self):
    """ Serializes the SelectedImage object into JSON """
    return {"instagram_user": self.instagram_user.username, "photo": self.photo}

class ImageUrl(models.Model):
  image_url   = models.URLField(max_length=300)
  upload_time = models.CharField(max_length=100)

class InstagramStory(models.Model):
  instagram_user  = models.ForeignKey(InstagramUser, default=None, on_delete=models.CASCADE)
  image_urls      = models.ManyToManyField(ImageUrl)
  upload_date     = models.CharField(max_length=100)
