from rest_framework import serializers
from django.core.exceptions import ValidationError

class PostImageToStorySerializer(serializers.Serializer):
	iusername = serializers.CharField(required=True)
	photo_url = serializers.CharField(required=True)

	def validate(self, data):
		iusername = data["iusername"]
		photo_url = data["photo_url"]

		if not iusername:
			raise ValidationError("A username is necessary for this operation")
		if not photo_url:
			raise ValidationError("A photo url is necessary for this operation")

		return data


