from django.db import models

# Create your models here.
class InstagramClient(models.Model):
  client_id = models.CharField(max_length=35)
  redirect_uri = models.CharField(max_length=300)

class AuthenticationToken(models.Model):
  token = models.CharField(max_length=100)
  date = models.DateTimeField('date acquired')