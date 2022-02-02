from django.http import HttpResponse, HttpRequest
import requests
from requests import Request
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def simple_route(request: HttpRequest):
	if request.method == 'GET' and HttpResponse.status_code == 200:
		return HttpResponse()
	if request.method != 'GET':
		return HttpResponse(405)

@csrf_exempt
def slug_route(*args, **kwargs):
	return HttpResponse(kwargs['val'][:-1])

@csrf_exempt
def sum_route(*args, **kwargs):
	print(args[-2], args[-1])
	return HttpResponse(sum(list(map(int, [args[-2], args[-1]]))))