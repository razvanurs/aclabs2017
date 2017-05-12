from django.shortcuts import render
from django import http

def hello(request):
    ip = request.META.get('REMOTE_ADDR')
    user = request.user.username
    return http.HttpResponse('Hello {u} from {ip}'.format(u=user, ip=ip))
# Create your views here.
