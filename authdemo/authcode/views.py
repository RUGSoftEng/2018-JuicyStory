from django.shortcuts import render
from .models import InstagramClient, AuthenticationToken
from django.utils import timezone


def get_auth_code(request):
  if 'code' in request.GET:
    newToken = AuthenticationToken(
        token=request.GET['code'], date=timezone.now())
    newToken.save()
  #   ret = {'code': request.GET['code']}
  # else:
  #   ret = {'error_message': 'No Code'}

  return render(request, 'admin')


def user_list(request):
  clients = InstagramClient.objects.values()
  context = {'user_list': clients}
  return render(request, 'authcode/user_list.html', context)

# def send_auth_request(request):
#   context = {'response_type':'code'}
#   if 'client_id' in request.GET and 'redirect_uri' in request.GET:
#     context['client_id'] = request.GET['client_id']
#     context['redirect_uri'] = request.GET['redirect_uri']

#   # return render(request, 'https://api.instagram.com/oauth/authorize', context)
#   # return HttpResponseRedirect('https://api.instagram.com/oauth/authorize', args=context)
#   return HttpResponseRedirect(reverse('https://api.instagram.com/oauth/authorize', kwargs=context))
