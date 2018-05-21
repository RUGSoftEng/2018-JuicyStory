from rest_framework import generics
from .models import InstagramUser
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from .serializers import InstagramUserSerializer
from rest_framework.filters import OrderingFilter

class RUDInstagramUser(generics.RetrieveUpdateDestroyAPIView):
	''' Api for RUD (read, update, delete) '''
	queryset 			= InstagramUser.objects.all()
	serializer_class 	= InstagramUserSerializer
	permission_classes 	= (IsAuthenticated,)
	lookup_field 		= 'username'

class FilterInstagramUser(generics.ListAPIView):
	''' Api for setting filters based on the field attributes below '''
	fields 				= ('id', 'username', 'password', 'owner')
	queryset 			= InstagramUser.objects.all()
	serializer_class 	= InstagramUserSerializer
	permission_classes 	= (IsAuthenticated,)
	filter_backends 	= (filters.DjangoFilterBackend, OrderingFilter)
	filter_fields 		= fields
