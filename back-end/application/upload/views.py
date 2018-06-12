from rest_framework.views import APIView
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import PostImageToStorySerializer
from .utils import upload_image, download_and_schedule_image


class PostImageToStory(APIView):
  ''' Post and image url directrly to instagram '''
  serializer_class = PostImageToStorySerializer
  permission_classes = (IsAuthenticated,)

  def post(self, request, *args, **kwargs):
    data = request.data
    serializer = PostImageToStorySerializer(data=data)

    if serializer.is_valid(raise_exception=True):
      valid_data = serializer.data
      iusername = valid_data["iusername"]
      photo_url = valid_data["photo_url"]
      download_and_schedule_image(photo_url, iusername, "2000-10-10", "00:00", is_story=True)
      return Response(valid_data, status=HTTP_200_OK)
    else:
      return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
