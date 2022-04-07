import base64

from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views import View
import json
from jsonschema.validators import validate
from jsonschema.exceptions import ValidationError
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate

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

        auth64 = request.META.get('HTTP_AUTHORIZATION')
        auth = base64.b64decode(auth64).decode('ascii')
        print(auth)
        username, password = auth.split(':')
        user = authenticate(username=username, password=password)
        if user is None:
            return JsonResponse({}, status=401)
        if not user.is_staff:
            return JsonResponse({}, status=403)
        try:
            data = json.loads(request.body)
            if 'price' in data.keys():
                data['price'] = int(data['price'])
            validate(data, ITEM_SCHEMA)
            item = Item(title=data['title'], description=data['description'], price=data['price'])
            item.save()
            return JsonResponse({'id': item.id}, status=201)
        except (ValidationError, json.JSONDecodeError, TypeError, ValueError) as exc:
            print(exc)
            return JsonResponse({}, status=400)


class PostReviewView(View):
    """View для создания отзыва о товаре."""

    def post(self, request, item_id):

        auth64 = request.META.get('HTTP_AUTHORIZATION')
        auth = base64.b64decode(auth64).decode('ascii')
        username, password = auth.split(':')
        user = authenticate(username=username, password=password)
        if user is None:
            return JsonResponse({}, status=401)
        if not user.is_staff:
            return JsonResponse({}, status=403)
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


class GetItemView(View):
    """View для получения информации о товаре.

    Помимо основной информации выдает последние отзывы о товаре, не более 5
    штук.
    """
    def get(self, request, item_id):

        auth64 = request.META.get('HTTP_AUTHORIZATION')
        auth = base64.b64decode(auth64).decode('ascii')
        username, password = auth.split(':')
        user = authenticate(username=username, password=password)
        if user is None:
            return JsonResponse({}, status=401)
        if not user.is_staff:
            return JsonResponse({}, status=403)
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

