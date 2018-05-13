from rest_framework import viewsets
from .models import InstagramUser, SelectedImage, ScheduledImage
from .serializers import InstagramUserSerializer, SelectedImageSerializer, ScheduledImageSerializer

class InstagramUserViewSet(viewsets.ModelViewSet):
	''' Make request to retrieve infromation about the instagram accounts stored '''
	queryset = InstagramUser.objects.all()
	serializer_class = InstagramUserSerializer

class SelectedImageViewSet(viewsets.ModelViewSet):
	''' Make request to retrieve infromation about the images selected by an instagram user, 
	these would be the images displayed in the story creator tab  '''
	queryset = SelectedImage.objects.all()
	serializer_class = SelectedImageSerializer

class ScheduledImageViewSet(viewsets.ModelViewSet):
	''' Make request to retrieve information about the images that are stored to be uploaded on a
	later date '''
	queryset = ScheduledImage.objects.all()
	serializer_class = ScheduledImageSerializer