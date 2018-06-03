from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import list_images
from .serializers import IncomingSerializer


class IncomingDMs(APIView):
  """ View that receives information based on the instagram user. """
  fields = ('iusername')
  serializer_class = IncomingSerializer
  lookup_field = fields

  def get(self, request, iusername):
    data = list_images(iusername, None, None, True)
    data = {'dm': data}
    return Response(data, status=HTTP_200_OK)
