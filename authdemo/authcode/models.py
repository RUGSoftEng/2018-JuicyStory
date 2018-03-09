from django.db import models

# Create your models here.
class User(models.Model):
  client_id = models.CharField(max_length=30)
  redirect_uri = models.CharField(max_length=100)
  