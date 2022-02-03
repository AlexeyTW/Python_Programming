from django.urls import path, re_path
from .views import simple_route, slug_route, sum_route, sum_get_method

urlpatterns = [
	path(r'simple_route/', simple_route),
	re_path(r'(?P<key>slug_route/)(?P<val>[\w-]{1,16}/)', slug_route),
	re_path(r'sum_route/(-?\d)\/(-?\d)\/', sum_route),
	re_path(r'sum_get_method/', sum_get_method)
]
