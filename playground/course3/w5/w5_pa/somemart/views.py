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


class PostReviewForm(Form):
    text = django.forms.CharField(max_length=1024, required=True)
    grade = django.forms.IntegerField(min_value=1, max_value=10, required=True)


@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):
    """View для создания товара."""

    def post(self, request: HttpRequest):
        # Здесь должен быть ваш код
        form = AddItemForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            item = Item(title=context['title'], description=context['description'], price=context['price'])
            item.save()
            return JsonResponse({'id': item.id}, status=201)
        else:
            print('Incorrect form')
            return JsonResponse({}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class PostReviewView(View):
    """View для создания отзыва о товаре."""

    def post(self, request, item_id):
        form = PostReviewForm(request.POST)
        if form.is_valid():
            if len(Item.objects.filter(id=item_id)) == 1:
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
        item = Item.objects.filter(id=item_id)[0]
        data = {
            'id': item_id,
            'title': item.title,
            'description': item.description,
            'price': item.price
        }
        reviews = Review.objects.filter(item_id=item_id).order_by('id')[:5]
        print(reviews)
        return JsonResponse({}, status=200)
