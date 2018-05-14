from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .utils import list_images, validate_ownership


class IncomingViewSet(viewsets.ViewSet):
  """ Viewset to handle requests made regarding the incoming images of instagram users. """

  def list(self, request):
    """ GET the list of incoming images for the given instagram user. """

    if "instagram_username" in request.GET:
      instagram_username = request.GET["instagram_username"]
    else:
      raise ValidationError(detail="instagram_username parameter is mandatory.")

    user = request.user
    if not validate_ownership(user, instagram_username):
      raise ValidationError(detail="You do not have permission for this operation.")

    tag = None
    location_id = None
    get_DM = None

    if "tag" in request.GET:
      tag = request.GET["tag"]

    if "location_id" in request.GET:
      location_id = request.GET["location_id"]

    if "get_DM" in request.GET:
      get_DM = request.GET["get_DM"]

    data = list_images(instagram_username, tag=tag, location_id=location_id, get_DM=get_DM)

    if "error" in data:
      return Response(data={"Error": data["error"]}, exception=True, status=400)

    return Response(data)


class LocationQueryViewSet(viewsets.ViewSet):
  """ Viewset to handle requests made to get location details """

  def list(self, request):
    """ GET the list of location names and their IDs for a passed location string. """

    if "location" in request.GET:
      location = request.GET["location"]
    else:
      raise ValidationError(detail="location parameter is mandatory.")

    count = 10  # the default value

    if "count" in request.GET:
      count = request.GET["count"]

    # data = query_locations_by_name(location)
    # COMMENTED OUT BECAUSE WE NEED EXTRA APP PERMISSIONS FOR THIS RIGHT NOW
    data = {"error": "Waiting for extra app permissions right now."}

    if "error" in data:
      return Response(data={"Error": data["error"]}, exception=True, status=400)

    return Response(data["data"][:count])
