from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
@login_required(login_url='/users/login/')
def addIuser(request):
	form = forms.AddIuser()
	return render(request, 'iusers/add-iuser.html', {'form':form})