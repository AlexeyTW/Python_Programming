from django.urls import path
from .views import simple_route

urlpatterns = [
	path(r'simple_route/', simple_route)
]
