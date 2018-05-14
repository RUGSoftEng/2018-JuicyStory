from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

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
