from django.shortcuts import render, get_object_or_404
from authcode.models import InstagramUser
from .utils import *
from .forms import ImageUploadForm


def process_image_upload(request, username):
  user = get_object_or_404(InstagramUser, username=username)

  if(request.method == 'POST'):
    pass

def upload_page(request, username):
  user = get_object_or_404(InstagramUser, username=username)

  form = ImageUploadForm()

  return render(request, 'upload/upload.html', {'form': form})
