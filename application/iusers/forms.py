from django import forms
# from . import models
from authentication.models import InstagramUser

class AddIuser(forms.ModelForm):
	class Meta:
		model = InstagramUser
		fields = ['username']