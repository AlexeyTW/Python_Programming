from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseBadRequest
from django.http.response import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

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
	if request.method == 'GET' and len(request.GET) != 0:
		try:
			a = int(request.GET['a'])
			b = int(request.GET['b'])
		except ValueError:
			return HttpResponseBadRequest()
		return HttpResponse(a + b)
	return HttpResponseNotAllowed('GET')

@csrf_exempt
def sum_post_method(request: HttpRequest):
	print(request.content_params)
	if request.method == 'POST' and len(request.GET) != 0:
		try:
			a = int(request.GET['a'])
			b = int(request.GET['b'])
		except ValueError:
			return HttpResponseBadRequest()
		return HttpResponse(a + b)
	return HttpResponseNotAllowed('POST')
