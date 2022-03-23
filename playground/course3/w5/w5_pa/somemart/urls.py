from django.conf.urls import url

from .views import AddItemView, GetItemView, PostReviewView

urlpatterns = [
    url('api/v1/goods/(\d+)/reviews', PostReviewView.as_view()),
    url('api/v1/goods/(\d+)/', GetItemView.as_view()),
    url('api/v1/goods/', AddItemView.as_view()),
]
