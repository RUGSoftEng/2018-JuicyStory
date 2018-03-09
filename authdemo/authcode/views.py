from django.shortcuts import render
from .models import User

def get_auth_code(request):
  if 'code' in request.GET:
    ret = {'code': request.GET['code']}
  else:
    ret = {'error_message': 'No Code'}

  return render(request, 'authcode/received.html', ret)

def user_list(request):
  users = User.objects.values()
  context = {'user_list':users}
  return render(request, 'authcode/user_list.html', context)