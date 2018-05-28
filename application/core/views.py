from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from database.models import InstagramUser

@login_required(login_url="/entry/login/")
def home(request, username):
	''' The view responsible for showing the default template '''
	instagram_user 	= get_object_or_404(InstagramUser, username=username)
	data 			= {'instagram_user' : instagram_user}
	return render(request, "base_layout.html", data)