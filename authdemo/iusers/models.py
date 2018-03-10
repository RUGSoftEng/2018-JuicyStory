from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Iusers(models.Model):
	username = models.CharField(max_length=50)
	owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)