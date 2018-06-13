from rest_framework import serializers


class InstagramUserSerializer(serializers.Serializer):
  username = serializers.CharField(max_length=30)
  time_since = serializers.CharField(max_length=30)
  time_until = serializers.CharField(max_length=30)
