from rest_framework import viewsets
from .models import InstagramUser, SelectedImage
from upload.models import Image
from .serializers import InstagramUserSerializer, SelectedImageSerializer, ImageSerializer

class InstagramUserViewSet(viewsets.ModelViewSet):
	queryset = InstagramUser.objects.all()
	serializer_class = InstagramUserSerializer

class SelectedImageViewSet(viewsets.ModelViewSet):
	queryset = SelectedImage.objects.all()
	serializer_class = SelectedImageSerializer

class ImageViewSet(viewsets.ModelViewSet):
	queryset = Image.objects.all()
	serializer_class = ImageSerializer