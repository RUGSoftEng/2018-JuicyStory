from rest_framework import viewsets
from .models import InstagramUser, SelectedImage, ScheduledImage
from .serializers import InstagramUserSerializer, ScheduledImageSerializer
from rest_framework.response import Response
from incoming.utils import validate_ownership  #TODO: Maybe move this into this module?
from rest_framework.exceptions import ValidationError


class InstagramUserViewSet(viewsets.ModelViewSet):
  ''' Make request to retrieve infromation about the instagram accounts stored.
  Returns only the accounts owned by the requesting user.
   '''
  queryset = InstagramUser.objects.all()
  serializer_class = InstagramUserSerializer

  def get_queryset(self):
    """ Filter for accounts owned by the requesting user """
    queryset = self.queryset
    query_set = queryset.filter(owner=self.request.user)
    return query_set

  def create(self, request):
    """ POST a new instagram user for the current user """

    try:
      instagram_user = InstagramUser(
        username=request.data["username"],
        password=request.data["password"],
        fbtoken=request.data["fbtoken"],
        fbid=request.data["fbid"],
        access_token=request.data["access_token"],
        owner=request.user)
      instagram_user.save()
      return Response("Success")

    except KeyError:
      raise ValidationError(detail={"error": "Not all necessary fields provided."})
    except:
      raise ValidationError(detail={"error": "Something went wrong."})


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


class ScheduledImageViewSet(viewsets.ModelViewSet):
  ''' Make request to retrieve information about the images that are stored to be uploaded on a
  later date '''
  queryset = ScheduledImage.objects.all()
  serializer_class = ScheduledImageSerializer