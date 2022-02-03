from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseBadRequest
from django.http import HttpResponseNotAllowed
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
	return HttpResponse(sum(list(map(int, [args[-2], args[-1]]))))

@csrf_exempt
def sum_get_method(request: HttpRequest):
	if request.method == 'GET' and request.GET['a'] and request.GET['b']:
		try:
			a = int(request.GET['a'])
			b = int(request.GET['b'])
		except ValueError:
			return HttpResponseBadRequest()
		return HttpResponse(a + b)
	return HttpResponseNotFound

@csrf_exempt
def sum_post_method(request: HttpRequest):
	print(request)
	if request.method == 'POST' and request.GET['a'] and request.GET['b']:
		try:
			a = int(request.GET.get('a'))
			b = int(request.GET.get('b'))
		except ValueError:
			return HttpResponseBadRequest()
		return HttpResponse(a + b)
	return HttpResponseNotFound
