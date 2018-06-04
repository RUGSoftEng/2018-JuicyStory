from rest_framework.views import APIView
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import PostImageToStorySerializer
from .utils import upload_image

class PostImageToStory(APIView):
  ''' def post(self, request, iuser, photo_url): '''
  serializer_class = PostImageToStorySerializer
  permission_classes = (IsAuthenticated,)

  def post(self, request, *args, **kwargs):
  	data = request.data
  	serializer = PostImageToStorySerializer(data=data)

  	if serializer.is_valid(raise_exception=True):
  		valid_data = serializer.data
  		iusername = valid_data["iusername"]
  		photo_url = valid_data["photo_url"]
  		upload_image(iusername, photo_url)
  		return Response(valid_data, status=HTTP_200_OK)
  	else:
  		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


