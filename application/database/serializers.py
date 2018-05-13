from rest_framework import serializers
from .models import InstagramUser, SelectedImage, ScheduledImage

''' Serializing the classes passing all the relevant objects to the viewsets '''

class InstagramUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = InstagramUser
		fields = '__all__'
		
class SelectedImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = SelectedImage
		fields = '__all__'

class ScheduledImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = ScheduledImage
		fields = '__all__'