from django.contrib import admin
from .models import (InstagramUser, SelectedImage, ScheduledImage, ImageUrl, InstagramStory)

admin.site.register(InstagramUser)
admin.site.register(SelectedImage)
admin.site.register(ScheduledImage)
admin.site.register(ImageUrl)
admin.site.register(InstagramStory)
