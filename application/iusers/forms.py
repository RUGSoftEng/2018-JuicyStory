from django import forms
from database.models import InstagramUser

class AddIuser(forms.ModelForm):
	''' A form class generating entry points for the database '''
	class Meta:
		model = InstagramUser
		fields = ['username']