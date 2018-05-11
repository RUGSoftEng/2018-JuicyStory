from rest_framework import serializers


class IncomingSerializer(serializers.Serializer):
    id = serializers.IntegerField()
