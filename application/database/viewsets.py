from .models import (InstagramUser, SelectedImage)
from .serializers import InstagramUserSerializer
from incoming.utils import validate_ownership  #TODO: Maybe move this into this module?

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

class SelectedImageViewSet(viewsets.ViewSet):
  """ Make request to retrieve information about the images selected by an instagram user, 
  these would be the images displayed in the story creator tab.
  Returns only the images selected by the requesting user. """

  def validate(self, request, post=None):
    """ Validates if the instagram user exists and it belongs to this user. 
    Throws an error if something is wrong. Returns the instagram user otherwise. """

    if "instagram_username" in request.GET:
      instagram_username = request.GET["instagram_username"]
    elif post and "instagram_username" in request.data:
      instagram_username = request.data["instagram_username"]
    else:
      raise ValidationError(detail="instagram_username parameter is mandatory.")

    if not validate_ownership(request.user, instagram_username):
      raise ValidationError(detail="You do not have permission for this.")

    return InstagramUser.objects.get(username=instagram_username)

  def list(self, request):
    """ GET the list of selected images for the given instagram user. """

    instagram_user = self.validate(request)
    selected_images = SelectedImage.objects.filter(instagram_user=instagram_user)

    serialized_result = []
    for image in selected_images:
      serialized_result.append(image.serialize())

    return Response(serialized_result)

  def create(self, request):
    """ POST a list of selected image for the given instagram_user.
    The expected JSON format is: {instagram_username:<USERNAME>, images:[<URL1>,<URL2>]} """

    instagram_user = self.validate(request, post=True)
    if "images" in request.data:
      for image_url in request.data["images"]:
        selected_image = SelectedImage(instagram_user=instagram_user, photo=image_url)
        selected_image.save()

      return Response("Success")

    else:
      raise ValidationError(detail={"error": "No images specified."})

  #TODO: Define a delete action
