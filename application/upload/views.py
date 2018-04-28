from django.shortcuts import render, get_object_or_404, redirect
from database.models import InstagramUser, SelectedImage
from .utils import download_schedule_image


def process_selected_images(request, iusername):
  if request.method == 'POST':
    action = request.POST['action']
    date = request.POST['date']
    time = request.POST['time']

    image_url = request.POST.getlist('url')
    for url in image_url:
      print(url)
      if action == 'Delete':
        SelectedImage.objects.filter(photo=url).delete()
      elif action == 'Upload':
        download_schedule_image(url, iusername, date, time)

  return redirect('upload:list_selected_images', iusername)


def list_selected_images(request, iusername):
  instagram_user = get_object_or_404(InstagramUser, username=iusername)
  images = SelectedImage.objects.filter(instagram_user=instagram_user)
  context = {'images': images, 'instagram_user': instagram_user}
  return render(request, 'upload/story_creator.html', context)
