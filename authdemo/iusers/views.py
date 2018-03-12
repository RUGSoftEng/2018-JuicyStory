from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from authcode.models import InstagramUser

# if the user calls the function from the urls, he will go to the else
# statement and show the html with the form. If he is already in the html
# and he submits then we redirect him to the page listing all instagram accs.
@login_required(login_url='/users/login/')
def add_iuser(request):
	if request.method == 'POST':
		form = forms.AddIuser(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.owner = request.user
			instance.save()
			return redirect('iusers:list_iusers')
	else:
		form = forms.AddIuser()
	return render(request, 'iusers/add-iuser.html', {'form':form})

@login_required(login_url='/users/login/')
def list_iusers(request):
	iusers = InstagramUser.objects.filter(owner=request.user)
	return render(request, 'iusers/iuser-list.html', {'iusers':iusers})