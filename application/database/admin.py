from django.contrib import admin
from .models import (InstagramUser, SelectedImage, ScheduledImage)

''' Register all the databases that are going to be accessible to the administrator '''
admin.site.register(InstagramUser)
admin.site.register(SelectedImage)
admin.site.register(ScheduledImage)
