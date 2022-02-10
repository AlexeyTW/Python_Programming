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
    return [None, None]


@csrf_exempt
def echo(request: HttpRequest):
    context = {'request_type': request.method.lower(),
               'param': get_param(request)[0] or 'None',
               'val': get_param(request)[1] or 'None',
               'statement': request.META[('HTTP_' + 'X_Print_Statement').upper()] if
                            ('HTTP_' + 'X_Print_Statement').upper() in request.META.keys()
                            else 'empty'
               }
    #print(TemplateResponse(request, 'echo.html', context).render().content.decode().strip())
    return TemplateResponse(request, 'echo.html', context)


def filters(request):
    context = {'a': request.GET.get('a', '10'),
        'b': request.GET.get('b', 1)}
    print(TemplateResponse(request, 'filters.html', context).render().content.decode().strip())
    return render(request, 'filters.html', context)


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
