from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def sign_up(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			#log the user in
			user = form.get_user()
			login(request, user)
			#bad way to redirect
			return redirect('http://127.0.0.1:8000/home/')
			#return HttpResponse("User logged in!")
	else:
		form = UserCreationForm()
	return render(request, "users/sign-up.html", {'form': form})

def log_in(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#log in the user
			user = form.get_user()
			login(request, user)
			#bad way to redirect.
			return redirect('http://127.0.0.1:8000/home/')
	else:
		form = AuthenticationForm()
	return render(request, "users/log-in.html", {'form': form})