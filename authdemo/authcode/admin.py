from django.contrib import admin
from .models import InstagramClient, AuthenticationToken
# Register your models here.

admin.site.register(InstagramClient)
admin.site.register(AuthenticationToken)