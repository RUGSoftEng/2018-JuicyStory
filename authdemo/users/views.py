from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def sign_up(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			#log the user in
			login(request, user)
			#bad way to redirect
			return redirect('iusers:list_iusers')
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
			return redirect('iusers:list_iusers')
	else:
		form = AuthenticationForm()
	return render(request, "users/log-in.html", {'form': form})

def log_out(request):
	if request.method == 'POST':
		logout(request)
		return redirect('users:login')
