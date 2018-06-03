from rest_framework import serializers


class InstagramUserSerializer(serializers.Serializer):
  username = serializers.CharField(max_length=30)
  timeSince = serializers.CharField(max_length=30)
  timeUntil = serializers.CharField(max_length=30)
