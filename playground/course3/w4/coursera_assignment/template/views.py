from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.template.response import TemplateResponse


# Create your views here.
def get_param(request: HttpRequest):
    if request.method == 'GET' and request.GET != {}:
        return list(request.GET.keys())[0]
    if request.method == 'POST' and request.POST != {}:
        return list(request.POST.keys())[0]


@csrf_exempt
def echo(request: HttpRequest):
    return TemplateResponse(request, 'echo.html', context={
        'request_type': request.method.lower(),
        'param': get_param(request),
        'val': '___'
    })


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
