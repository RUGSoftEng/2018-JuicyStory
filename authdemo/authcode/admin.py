from django.contrib import admin

from .models import InstagramClient, InstagramUser
from upload.models import Image

admin.site.register(InstagramClient)
admin.site.register(InstagramUser)
admin.site.register(Image)

