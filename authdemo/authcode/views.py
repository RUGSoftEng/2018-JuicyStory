from django.shortcuts import render
from .models import User
# from django.http import HttpResponseRedirect
# from django.urls import reverse


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

# def send_auth_request(request):
#   context = {'response_type':'code'}
#   if 'client_id' in request.GET and 'redirect_uri' in request.GET:
#     context['client_id'] = request.GET['client_id']
#     context['redirect_uri'] = request.GET['redirect_uri']    

#   # return render(request, 'https://api.instagram.com/oauth/authorize', context)
#   # return HttpResponseRedirect('https://api.instagram.com/oauth/authorize', args=context)
#   return HttpResponseRedirect(reverse('https://api.instagram.com/oauth/authorize', kwargs=context))