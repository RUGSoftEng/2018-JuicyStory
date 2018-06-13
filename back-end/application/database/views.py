from rest_framework.generics import (CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST)
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters

from .models import (InstagramUser, InstagramStory)
from .serializers import (InstagramUserSerializer, InstagramStorySerializer, CreateInstagramStorySerializer, CreateInstagramStoryUrlSerializer)


class CreateInstagramUser(CreateAPIView):
  ''' Api that allows for the creation of an instagram account object
  that is going to be stored in the database. '''
  queryset = InstagramUser.objects.all()
  serializer_class = InstagramUserSerializer


class RUDInstagramUser(RetrieveUpdateDestroyAPIView):
  ''' Api for RUD (read, update, delete) '''
  queryset = InstagramUser.objects.all()
  serializer_class = InstagramUserSerializer
  lookup_field = 'username'


class FilterInstagramUser(ListAPIView):
  ''' Api for setting filters based on the field attributes below '''
  fields = ['username',]
  queryset = InstagramUser.objects.all()
  serializer_class = InstagramUserSerializer
  filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
  filter_fields = fields

class CreateInstagramStoryUrl(APIView):
  serializer_class  = CreateInstagramStoryUrlSerializer

  def post(self, request, *args, **kwargs):
    data        = request.data
    serializer  = CreateInstagramStoryUrlSerializer(data=data)

    if serializer.is_valid(raise_exception=True):
      return Response(serializer.data, status=HTTP_200_OK)
    else:
      return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class CreateInstagramStories(CreateAPIView):
  queryset          = InstagramStory.objects.all()
  serializer_class  = CreateInstagramStorySerializer

class RUDInstagramStories(RetrieveUpdateDestroyAPIView):
  ''' Api for RUD (read, update, delete) '''
  queryset          = InstagramStory.objects.all()
  serializer_class  = InstagramStorySerializer
  lookup_field      = 'username'

class FilterInstagramStories(ListAPIView):
  ''' Api for retireving information regarding the instagram story urls '''
  queryset          = InstagramStory.objects.all()
  serializer_class  = InstagramStorySerializer
  filter_backends   = (filters.DjangoFilterBackend,)
  filter_fields     = [
    'username',
  ]