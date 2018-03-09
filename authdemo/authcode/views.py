from django.shortcuts import render


def get_auth_code(request):
  if 'code' in request.GET:
    ret = {'code': request.GET['code']}
  else:
    ret = {'error_message': 'No Code'}

  return render(request, 'authcode/received.html', ret)
