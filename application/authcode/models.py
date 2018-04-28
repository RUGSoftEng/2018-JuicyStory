from django.db import models
from django.contrib.auth.models import User

class InstagramUser(models.Model):
  username = models.CharField(max_length=30)
  password = models.CharField(max_length=50)
  access_token = models.CharField(max_length=100, blank=True)
  owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

# Images that are selected by an instagramUser
class SelectedImage(models.Model):
	instagram_user = models.ForeignKey(InstagramUser, default=None, on_delete=models.CASCADE)
	photo = models.CharField(max_length=300)