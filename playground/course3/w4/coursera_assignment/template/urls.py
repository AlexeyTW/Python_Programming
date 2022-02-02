from django.urls import path

from .views import echo, filters, extend

urlpatterns = [
    path(r'^echo/$', echo),
    path(r'^filters/$', filters),
    path(r'^extend/$', extend),
]
