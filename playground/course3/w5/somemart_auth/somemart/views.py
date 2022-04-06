from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views import View
import json
from jsonschema.validators import validate
from jsonschema.exceptions import ValidationError
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Item, Review

ITEM_SCHEMA = {
    '#schema': 'https://json-schema.org/schema#',
    'type': 'object',
    'properties': {
        'title': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 64,
        },
        'description': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 1024
        },
        'price': {
            'type': 'integer',
            'minimum': 1,
            'maximum': 100000
        }
    },
    'required': ['title', 'description', 'price']
}


@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):
    """View для создания товара."""

    def post(self, request: HttpRequest):
        try:
            print(request.META.get('HTTP_AUTHORIZATION'))
            return JsonResponse({}, status=201)
        except (ValidationError, json.JSONDecodeError, TypeError, ValueError):
            return JsonResponse({}, status=400)
        #return JsonResponse(data, status=201)


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
