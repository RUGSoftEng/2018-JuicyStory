from rest_framework import serializers
from .models import (InstagramUser, ImageUrl, InstagramStory)
from django.core.exceptions import ValidationError


class InstagramUserSerializer(serializers.ModelSerializer):

  class Meta:
    model 	= InstagramUser
    fields 	= '__all__'

class ImageUrlSelrializer(serializers.ModelSerializer):
	''' Serializer for the purpuse of excluding the 'id' form the nested fields. '''
	class Meta:
		model 	= ImageUrl
		exclude = ['id',]

class InstagramStorySerializer(serializers.ModelSerializer):

	image_urls 	= ImageUrlSelrializer(many=True, read_only=True)

	class Meta:
		model 	= InstagramStory
		fields  = [
			'image_urls',
			'upload_date',
		]
		depth 	= 1

class CreateInstagramStorySerializer(serializers.ModelSerializer):

	class Meta:
		model 	= InstagramStory
		fields 	= [
			'username',
			'upload_date',
		]

class CreateInstagramStoryUrlSerializer(serializers.ModelSerializer):
	username 	= serializers.CharField(required=True, allow_blank=False)
	upload_date = serializers.CharField(required=True, allow_blank=False)
	image_url 	= serializers.URLField(required=True, max_length=300)
	upload_time = serializers.CharField(required=True, allow_blank=False)

	class Meta:
		model 	= InstagramStory
		fields 	= [
			'username',
			'upload_date',
			'image_url',
			'upload_time',
		]

	def validate(self, data):
		username 	= data["username"]
		upload_date = data["upload_date"]
		image_url 	= data["image_url"]
		upload_time = data["upload_time"]
		queryset    = InstagramStory.objects.all()

		if not queryset.filter(username=username).exists():
			raise ValidationError("Username does not exist.")
		elif not queryset.filter(upload_date=upload_date).exists():
			raise ValidationError("Date is not valid.")

		instagram_story = None
		instagram_story = InstagramStory.objects.get(username=username, upload_date=upload_date)

		if instagram_story is None:
			raise ValidationError("The username and upload_date combination is incorrect.")

		image = ImageUrl()
		image.image_url = image_url
		image.upload_time = upload_time
		image.save()
		instagram_story.image_urls.add(image)
		instagram_story.save()

		return data
