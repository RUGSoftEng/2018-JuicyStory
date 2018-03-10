from django import forms
from . import models

class AddIuser(forms.ModelForm):
	class Meta:
		model = models.Iusers
		fields = ['username']