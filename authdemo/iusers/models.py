from django.db import models

# Create your models here.
class Iusers(models.Model):
	username = models.CharField(max_length=50)