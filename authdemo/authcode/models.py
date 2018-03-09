from django.db import models

# We currently have only one client
class InstagramClient(models.Model):
  client_id = models.CharField(max_length=50)
  client_secret = models.CharField(max_length=50, default="")
  redirect_uri = models.CharField(max_length=300)

# Boaty Macboatface only currently
class InstagramUser(models.Model):
  username = models.CharField(max_length=30)
  access_token = models.CharField(max_length=100)
