
from django.urls import path
from .views import FormDummyView

urlpatterns = [
    path('form/', FormDummyView.as_view())
]
