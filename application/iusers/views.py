from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from database.models import InstagramUser

@login_required(login_url='/entry/login/')
def list_iusers(request):
	''' This view serves both the creation of an instagram 
	account and the redirect after submitting an account '''
	if request.method == 'POST':
		form = forms.AddIuser(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.owner = request.user
			instance.save()
			return redirect('iusers:list_iusers')
	else:
		form = forms.AddIuser()
	iusers = InstagramUser.objects.filter(owner=request.user)
	return render(request, 'iusers/iuser-list.html', {'iusers':iusers, 'form':form})