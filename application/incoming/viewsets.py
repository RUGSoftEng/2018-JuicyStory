from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .utils import list_images


class IncomingViewSet(viewsets.ViewSet):
    """ Viewset to handle requests made regarding the incoming images of instagram users. """

    def list(self, request):
        """ GET the list of incoming images for the given instagram user. """

        if "instagram_user_name" in request.GET:
            instagram_user_name = request.GET["instagram_user_name"]
        else:
            raise ValidationError(
                detail="instagram_user_name parameter is mandatory.")

        data = list_images(instagram_user_name, tag="cat")

        if "Error" in data:
            return ValidationError(detail=data["Error"])

        return Response(data)
