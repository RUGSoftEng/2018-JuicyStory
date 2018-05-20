from rest_framework import serializers
from .models import InstagramUser, ScheduledImage


class InstagramUserSerializer(serializers.ModelSerializer):
	
  class Meta:
    model = InstagramUser
    fields = '__all__'
