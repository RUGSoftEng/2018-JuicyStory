from rest_framework import serializers
from .models import InstagramUser, SelectedImage
from upload.models import Image

class InstagramUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = InstagramUser
		fields = '__all__'
		
class SelectedImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = SelectedImage
		fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = '__all__'