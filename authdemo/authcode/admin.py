from django.contrib import admin
from .models import InstagramClient, InstagramUser
# Register your models here.

admin.site.register(InstagramClient)
admin.site.register(InstagramUser)