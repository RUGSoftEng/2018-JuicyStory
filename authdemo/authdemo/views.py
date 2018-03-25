from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from authcode.models import InstagramUser

#this will redirect us to the login page
@login_required(login_url="/users/login/")
def home(request, username):
	instagram_user = get_object_or_404(InstagramUser, username=username)
	return render(request, "home.html", {'instagram_user':instagram_user})