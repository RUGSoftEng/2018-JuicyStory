from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from authcode.models import InstagramUser
from .forms import ImageUploadForm
from .models import Image


def upload_page(request, username):
  user = get_object_or_404(InstagramUser, username=username)
  context = {'username': user.username}

  if(request.method == 'POST'):
    form = ImageUploadForm(request.POST, request.FILES)
    if form.is_valid:
      newImage = Image(username=user.username,
                       image_file=request.FILES['file'], upload_date=request.POST['upload_date'], is_story=(True if request.POST['upload_type'] == 'story' else False))
      newImage.save()

      return HttpResponseRedirect(reverse('upload:upload_page', kwargs=context))
  else:
    form = ImageUploadForm()

  context['form'] = form

  return render(request, 'upload/upload.html', context)
