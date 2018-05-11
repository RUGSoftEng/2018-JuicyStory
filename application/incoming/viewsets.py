from .serializer import IncomingSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class IncomingViewSet(viewsets.ViewSet):

  def list(self, request):
    data = [{'id': 1}]
    results = IncomingSerializer(data, many=True).data
    return Response(results)
