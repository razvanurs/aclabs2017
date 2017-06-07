import json
import os

from django.shortcuts import render, redirect
from django import http
from django.db.models import F
from .models import Poll, Choice, Question

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
	polls_qs = Poll.objects.values('name', 'slug')
	
	return render(request, 'polls_app/index.html', context={'polls': polls_qs})
	
	
def detail(request, slug):
	if request.method == 'POST':
		# return redirect('index')
		for key, value in request.POST.items():
			if key.startswith('question-'):
				Choice.objects.filter(pk=value).update(votes=F('votes') + 1)
		return redirect('result', slug=slug)
	try:
		poll = Poll.objects.prefetch_related('questions__choice_set').get(slug=slug)
	except Poll.DoesNotExist:
		print('dsa')
		return http.HttpResponse(content='Poll not found', status=404)
	
	return render(request, 'polls_app/detail.html', context={'poll': poll})
	

def result(request, slug):
		try:
			poll = Poll.objects.prefetch_related('questions__choice_set').get(slug=slug)
		except Poll.DoesNotExist:
			return http.HttpResponse(content='Poll not found', status=404)
		return render(request, 'polls_app/result.html', {"poll": poll})
	
	
def clear(request, slug):
	questions = Question.objects.filter(poll__slug=slug)
	# toate choices care au question in poll.questions
	Choice.objects.filter(question__in=questions).update(votes=0)
	
	# poll = Poll.objects.get(slug=slug)
	# for question in poll.questions.all():
	#	question.choice_set.all().update(votes=0)
	
	return redirect('result', slug=slug)
