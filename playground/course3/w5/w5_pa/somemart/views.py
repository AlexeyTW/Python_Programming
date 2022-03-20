import json

import django.forms
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms import Form

from .models import Item, Review

class AddItemForm(Form):
    title = django.forms.CharField(label='title', max_length=64, required=True)
    description = django.forms.CharField(label='description', max_length=1024, required=True)
    price = django.forms.IntegerField(label='price', min_value=1, max_value=100000, required=True)


@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):
    """View для создания товара."""

    def post(self, request: HttpRequest):
        # Здесь должен быть ваш код
        form = AddItemForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            print(context)
            return HttpResponse('12345', status=201)

        else:
            print('!!!')
            return HttpResponse(request)
        #return JsonResponse('data', status=201)


class PostReviewView(View):
    """View для создания отзыва о товаре."""

    def post(self, request, item_id):
        # Здесь должен быть ваш код
        return JsonResponse(data, status=201)


class GetItemView(View):
    """View для получения информации о товаре.

    Помимо основной информации выдает последние отзывы о товаре, не более 5
    штук.
    """

    def get(self, request, item_id):
        # Здесь должен быть ваш код
        return JsonResponse(data, status=200)
