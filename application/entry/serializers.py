from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.models import Q	
from .utils import get_jwt_token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model 	= User
		fields 	= [
			'username',
			'password',
		]
		extra_kwargs = {
			'password': {'write_only': True}
		}

	def create(self, validated_data):
		username 	= validated_data['username']
		password 	= validated_data['password']

		user_object = User(username=username)
		user_object.set_password(password)
		user_object.save()

		return validated_data

class UserLoginSerializer(serializers.ModelSerializer):
	username 	= serializers.CharField(required=True, allow_blank=False)
	token 		= serializers.CharField(allow_blank=True, read_only=True)
	class Meta:
		model 	= User
		fields 	= [
			'username',
			'password',
			'token',
		]
		extra_kwargs = {
			'password': {'write_only': True}
		}

	def validate(self, data):
		validated_user 	= None
		username 		= data["username"]
		password 		= data["password"]

		if not username:
			raise ValidationError("A username is required to login.")
		user = User.objects.filter(Q(username=username)).distinct()

		if user.exists() and user.count() == 1:
			validated_user = user.first()
		else:
			raise ValidationError("This username is not valid.")

		if validated_user:
			if not validated_user.check_password(password):
				raise ValidationError("This password is incorrect.")
		data["token"] = get_jwt_token(username, password)
		return data



















