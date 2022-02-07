from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseBadRequest
from django.http.response import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def simple_route(request: HttpRequest):
	if request.method == 'GET' and HttpResponse.status_code == 200:
		return HttpResponse()
	if request.method != 'GET':
		return HttpResponseNotAllowed('GET')

@csrf_exempt
def slug_route(*args, **kwargs):
	return HttpResponse(kwargs['val'][:-1])

@csrf_exempt
def sum_route(request, *args, **kwargs):
	print(args, kwargs)
	return HttpResponse(sum(list(map(int, [args[-2], args[-1]]))))

@csrf_exempt
def sum_get_method(request: HttpRequest):
	if request.method == 'GET':
		if len(request.GET) == 2:
			try:
				a = int(request.GET['a'])
				b = int(request.GET['b'])
			except ValueError:
				return HttpResponseBadRequest()
			return HttpResponse(a + b)
		else:
			return HttpResponseBadRequest()
	return HttpResponseNotAllowed('GET')

@csrf_exempt
def sum_post_method(request: HttpRequest):
	print(type(request.get_raw_uri()))
	if request.method == 'POST' and request.get_raw_uri().endswith('sum_post_method/'):
		if len(request.POST) == 2:
			a = request.POST.get('a')
			b = request.POST.get('b')
			try:
				a = int(a)
				b = int(b)
			except ValueError:
				return HttpResponseBadRequest()
			return HttpResponse(sum([a, b]))
		else:
			return HttpResponseBadRequest()
	else:
		return HttpResponseNotAllowed('POST')
