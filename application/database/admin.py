from django.contrib import admin
from .models import InstagramUser, SelectedImage, Image

admin.site.register(InstagramUser)
admin.site.register(SelectedImage)
admin.site.register(Image)
