from rest_framework import serializers


class IncomingSerializer(serializers.Serializer):
  iusername = serializers.CharField(max_length=30)
