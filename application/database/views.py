from rest_framework import generics
from .models import InstagramUser
from django_filters import rest_framework as filters
from .serializers import InstagramUserSerializer
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.
class InstagramUserView(generics.ListAPIView):
	fields 				= ('id', 'username', 'password', 'owner')
	queryset 			= InstagramUser.objects.all()
	serializer_class 	= InstagramUserSerializer
	filter_backends 	= (filters.DjangoFilterBackend, OrderingFilter)
	filter_fields 		= fields

	'''def filter_queryset(self, queryset):
		Testing complexity 
		username = self.request.query_params.get('username',None)
		print(username)
		return queryset
		if username is not None:
			return queryset.filter(username=username)'''
