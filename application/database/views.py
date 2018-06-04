from rest_framework.generics import (CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters

from .models import InstagramUser
from .serializers import InstagramUserSerializer


class CreateInstagramUser(CreateAPIView):
  ''' Api that allows for the creation of an instagram account object
  that is going to be stored in the database. '''
  queryset = InstagramUser.objects.all()
  serializer_class = InstagramUserSerializer
  permission_classes = (IsAuthenticated,)


class RUDInstagramUser(RetrieveUpdateDestroyAPIView):
  ''' Api for RUD (read, update, delete) '''
  queryset = InstagramUser.objects.all()
  serializer_class = InstagramUserSerializer
  permission_classes = (IsAuthenticated,)
  lookup_field = 'username'


class FilterInstagramUser(ListAPIView):
  ''' Api for setting filters based on the field attributes below '''
  fields = ('id', 'username', 'password', 'owner')
  queryset = InstagramUser.objects.all()
  serializer_class = InstagramUserSerializer
  permission_classes = (IsAuthenticated,)
  filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
  filter_fields = fields
