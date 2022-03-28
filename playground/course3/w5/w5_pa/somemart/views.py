import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

import django.forms
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms import Form
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

REVIEW_SCHEMA = {
    '#schema': 'https://json-schema.org/schema#',
    'type': 'object',
    'properties': {
        'text': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 1024,
        },
        'grade': {
            'type': 'integer',
            'minimum': 1,
            'maximum': 10,
        },
    },
    'required': ['text', 'grade']
}


@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):
    """View для создания товара."""

    def post(self, request: HttpRequest):
        # Здесь должен быть ваш код
        try:
            data = json.loads(request.body)
            if 'price' in data.keys():
                data['price'] = int(data['price'])
            validate(data, ITEM_SCHEMA)
            item = Item(title=data['title'], description=data['description'], price=data['price'])
            item.save()
            return JsonResponse({'id': item.id}, status=201)
        except (ValidationError, json.JSONDecodeError, TypeError, ValueError):
            return JsonResponse({}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class PostReviewView(View):
    """View для создания отзыва о товаре."""

    def post(self, request, item_id):
        try:
            data = json.loads(request.body)
            if 'grade' in data.keys():
                data['grade'] = int(data['grade'])
            validate(data, REVIEW_SCHEMA)
            if len(Item.objects.filter(id=item_id)):
                added_item = Item.objects.filter(id=item_id)[0]
                review = Review(text=data['text'], grade=data['grade'], item=added_item)
                review.save()
                return JsonResponse({'id': review.id}, status=201)
            else:
                return HttpResponse('No item with such ID', status=404)
        except (ValidationError, json.JSONDecodeError, TypeError, ValueError):
            return HttpResponse('Validation error', status=400)


@method_decorator(csrf_exempt, name='dispatch')
class GetItemView(View):
    """View для получения информации о товаре.

    Помимо основной информации выдает последние отзывы о товаре, не более 5
    штук.
    """

    def get(self, request, item_id):
        # Здесь должен быть ваш код
        if len(Item.objects.filter(id=item_id)):
            item = Item.objects.filter(id=item_id)[0]
            reviews_obj = Review.objects.filter(item_id=item_id).order_by('-id')[:5]
            reviews = []
            for review in reviews_obj:
                r = {}
                r['id'] = review.__dict__['id']
                r['text'] = review.__dict__['text']
                r['grade'] = int(review.__dict__['grade'])
                reviews.append(r)

            data = {
                'id': int(item_id),
                'title': item.title,
                'description': item.description,
                'price': int(item.price),
                'reviews': reviews
            }
            return JsonResponse(data, status=200)
        else:
            return HttpResponse('Item with id {} does not exist'.format(item_id), status=404)
