from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#this will redirect us to the login page
@login_required(login_url="/users/login/")
def home(request):
	return render(request, "home.html")