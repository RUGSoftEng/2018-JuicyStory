from django import forms


class ImageUploadForm(forms.Form):
  file = forms.FileField(label="File to Upload")
  upload_date = forms.DateTimeField()
  upload_type = forms.ChoiceField(
      choices=[('story', 'story'), ('post', 'post')], widget=forms.RadioSelect())
