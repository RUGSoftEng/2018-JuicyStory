from django.contrib import admin
from .models import InstagramClient, InstagramUser, SelectedImage
from upload.models import Image


admin.site.register(InstagramClient)
admin.site.register(InstagramUser)
admin.site.register(SelectedImage)
admin.site.register(Image)
