from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny, IsAdminUser)
from django.http import QueryDict
from .serializers import (UserSerializer, UserLoginSerializer)

User = get_user_model()


class CreateUser(CreateAPIView):
  serializer_class = UserSerializer
  permission_classes = [IsAdminUser]
  queryset = User.objects.all()


class LoginUser(APIView):
  serializer_class = UserLoginSerializer
  permission_classes = [AllowAny]

  def post(self, request, *args, **kwargs):
    data        = request.data
    serializer  = UserLoginSerializer(data=data)

    if serializer.is_valid(raise_exception=True):
      valid_data = serializer.data
      print(valid_data)
      return Response(valid_data, status=HTTP_200_OK)
    else:
      return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

  def to_QueryDictionary(data):
    if not isinstance(data, QueryDict):
      query_dict = QueryDict('', mutable=True)
      query_dict.update(data)
      data = query_dict
    return data
