import json
import os

from django.shortcuts import render, redirect
from django import http

def read_datafile():
    filepath = os.path.join(os.path.dirname(__file__), 'polls.json')
    with open(filepath) as fp:
        return json.loads(fp.read())


DATA = read_datafile()


def hello(request):
    ip = request.META.get('REMOTE_ADDR')
    user = request.user.username
    return http.HttpResponse('Hello {u} from {ip}'.format(u=user, ip=ip))


def index(request):
    return render(request, 'polls_app/index.html', context={'polls': DATA})	
	
def detail(request, poll_name):
	if request.method == 'POST':
		return redirect('index')
	
	poll = next((poll for poll in DATA if poll['pollName'] == poll_name))
	
	return render(request, 'polls_app/detail.html', context={'poll': poll})
