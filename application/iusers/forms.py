from django import forms
from database.models import InstagramUser

class AddIuser(forms.ModelForm):
	class Meta:
		model = InstagramUser
		fields = ['username']