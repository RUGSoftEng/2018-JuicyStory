from django.contrib import admin

from .models import InstagramClient, InstagramUser, SelectedImage
# Register your models here.

admin.site.register(InstagramClient)
admin.site.register(InstagramUser)
admin.site.register(SelectedImage)

