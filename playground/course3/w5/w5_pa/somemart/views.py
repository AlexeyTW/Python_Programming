import json

import django.forms
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


class PostReviewForm(Form):
    text = django.forms.CharField(max_length=1024, required=True)
    grade = django.forms.IntegerField(min_value=1, max_value=10, required=True)


@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):
    """View для создания товара."""

    def post(self, request: HttpRequest):
        # Здесь должен быть ваш код
        form = AddItemForm(request.POST)
        print(request.body)
        if form.is_valid():
            context = form.cleaned_data
            item = Item(title=context['title'], description=context['description'], price=context['price'])
            item.save()
            return JsonResponse({'id': item.id}, status=201)
        else:
            return JsonResponse({}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class PostReviewView(View):
    """View для создания отзыва о товаре."""

    def post(self, request, item_id):
        form = PostReviewForm(request.POST)
        if form.is_valid():
            if len(Item.objects.filter(id=item_id)):
                context = form.cleaned_data
                added_item = Item.objects.filter(id=item_id)[0]
                review = Review(text=context['text'], grade=context['grade'], item=added_item)
                review.save()
                return JsonResponse({'id': review.id}, status=201)
            else:
                return HttpResponse('No item with such ID', status=404)
        else:
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
            print(data)
            return JsonResponse(data, status=200)
        else:
            return HttpResponse('Item with id {} does not exist'.format(item_id), status=404)
