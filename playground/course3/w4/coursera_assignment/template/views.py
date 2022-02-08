from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.template.response import TemplateResponse
from django.template import loader


# Create your views here.
def get_param(request: HttpRequest):
    if request.method == 'GET' and request.GET != {}:
        key = next(iter(request.GET.dict()))
        val = request.GET[key]
        return key, val
    if request.method == 'POST' and request.POST != {}:
        key = next(iter(request.POST.dict()))
        val = request.POST[key]
        return key, val
    return None


@csrf_exempt
def echo(request: HttpRequest):
    context = {'request_type': request.method.lower(),
               'param': get_param(request)[0],
               'val': get_param(request)[1]
               }
    #print(TemplateResponse(request, 'echo.html', context).render().content.decode())
    request.META['X-Print-Statement'] = 'test'
    print(request.META['X-Print-Statement'])
    return TemplateResponse(request, 'echo.html', context)


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
