from django.http import HttpResponse, HttpRequest
import requests
from requests import Request
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def simple_route(request: HttpRequest):
	#print(request.method, type(request.method))
	#if HttpResponse.status_code == 200:
		#return HttpResponse()
	if request.method == 'GET':
		print('Not get')
		return HttpResponse(405)
