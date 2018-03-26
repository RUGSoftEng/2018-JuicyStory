from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from authcode.models import InstagramUser, SelectedImage
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

#Remove an image from the database and refresh
def remove_selected_images(request, iusername):
  image_url = request.POST.get('url')
  SelectedImage.objects.filter(photo=image_url).delete()
  return redirect('upload:list_selected_images', iusername)

# display information based on user
def list_selected_images(request, iusername):
  instagram_user = get_object_or_404(InstagramUser, username=iusername)
  images = SelectedImage.objects.filter(instagram_user=instagram_user)
  context = {'images': images, 'instagram_user':instagram_user}
  return render(request, 'upload/list_selected_images.html', context)
