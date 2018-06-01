from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny, IsAdminUser)

from django.http import QueryDict
from .serializers import (UserSerializer, UserLoginSerializer)

User = get_user_model()

class CreateUser(CreateAPIView):
	serializer_class 	= UserSerializer
	permission_classes 	= [IsAdminUser]
	queryset 			= User.objects.all()

class LoginUser(APIView):
	serializer_class 	= UserLoginSerializer
	permission_classes 	= [AllowAny]

	def post(self, request, *args, **kwargs):
		data 		= request.data
		serializer 	= UserLoginSerializer(data=data)

		if serializer.is_valid(raise_exception=True):
			valid_data = serializer.data
			print(valid_data)
			return Response(valid_data, status=HTTP_200_OK)
		else:
			return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

	def to_QuetDictionary(data):
		if not isinstance(data, QueryDict):
				query_dict = QueryDict('', mutable=True)
				query_dict.update(data)
				data = query_dict
		return data

def sign_up(request):
	'''
	Method to sign-up the user after he
	has filled all the necessary fields
	in the form.
	'''
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			#log the user in
			login(request, user)
			return redirect('iusers:list_iusers')
	else:
		form = UserCreationForm()
	return render(request, "entry/sign-up.html", {'form': form})

def log_in(request):
	'''
	Method to log-in the user after 
	he has filled his credentials and
	is verified in the database. If the
	user is already authenticated we 
	redirect him to the list of iusers.
	'''
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#log in the user
			user = form.get_user()
			login(request, user)
			return redirect('iusers:list_iusers')
	else:
		if request.user.is_authenticated:
			return redirect('iusers:list_iusers')
		form = AuthenticationForm()
	return render(request, "entry/log-in.html", {'form': form})

def log_out(request):
	'''
	Method to log-out the user after
	he is already loged into the app.
	'''
	if request.method == 'POST':
		logout(request)
		return redirect('entry:login')
