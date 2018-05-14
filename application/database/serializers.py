from rest_framework import serializers
from .models import InstagramUser, ScheduledImage


class InstagramUserSerializer(serializers.ModelSerializer):

  class Meta:
    model = InstagramUser
    fields = '__all__'


class ScheduledImageSerializer(serializers.ModelSerializer):

  class Meta:
    model = ScheduledImage
    fields = '__all__'
